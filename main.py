from pandas import DataFrame, concat, Series, merge

import orizonDB
# from HKT import learning

def subtract_dates(data1, data2):
    # Subtracts2 strings that represent dates

    # Remove separators
    ano1, mes1, dia1 = data1.split('-')
    ano2, mes2, dia2 = data2.split('-')
    dAno = int(ano1) - int(ano2)
    dMes = int(mes1) - int(mes2)
    dDia = int(dia1) - int(dia2)
    return dDia + 30*dMes + 365*dAno

def get_history(analysisDB, id_):
    sexo = analysisDB['sexo'][id_]
    if sexo is not int: # Checks for repetitions
        sexo = sexo.values[0]
    historico = analysisDB.loc[[id_], ['data_item', 'servico', 'carater_atendimento', 'tipo_guia']] #histórico de procedimentos
    datas = [value.split(' ')[0] for value in historico['data_item']] # datas de procedimentos
    datas.sort()
    if len(datas) == 1:
        media = 0
        mediana = 0
    else:
        delta_datas = []
        for i in range(1, len(datas)):
            delta_datas.append(subtract_dates(datas[i], datas[i-1]))

        # media e mediana das distâncias entre visitas
        mediana = delta_datas[len(delta_datas)//2 ]
        media = 0
        for d in delta_datas:
            media += d

        media /= len(delta_datas)
    data_nascimento = analysisDB['data_nascimento'][id_]
    if data_nascimento is not str:
        data_nascimento = data_nascimento.values[0]
    idade = subtract_dates(datas[-1], data_nascimento)
    servicos = historico['servico'].values

    # Pega soma_servicos como vetor
    soma_servicos = [0]*len([value.strip('[,]') for value in servicos[0].split(' ')])
    for servico in servicos:
        servico = [value.strip('[,]') for value in servico.split(' ')]
        for i in range(len(servico)):
            soma_servicos[i] += int(servico[i])

    # Pega guias como vetores
    guias = historico['tipo_guia'].values
    soma_guias = [0]*len([value.strip('[]') for value in guias[0].split(',')])
    for guia in guias:
        guia = [value.strip('[]') for value in guia.split(',')]
        for i in range(len(guia)):
            soma_guias[i] += int(guia[i])

    # Soma dos caráters de atendimento
    caraters = historico['carater_atendimento'].values
    soma_carater = 0
    for carater in caraters:
        soma_carater += carater

    # Vetor representativo do histórico
    data = soma_servicos+[sexo]+[idade//365]+[media]+[mediana]+soma_guias+[soma_carater]
    return data

def main():
    mainDB = orizonDB.get_DB()[:10000] # Primeiros 10 mil para testes
    relevant_columns = ['id_beneficiario', # Pega só as colunas relevantes
                        'carater_atendimento',
                        'valor_item',
                        'tipo_guia',
                        'sexo',
                        'data_nascimento',
                        'data_item',
                        'senha',
                        'servico']
    print("DB separada")
    analysisDB = mainDB[relevant_columns]
    size = analysisDB.shape[0]

    # Transforma os parâmetros string em binários ou hot encoding
    analysisDB["carater_atendimento"].replace(["URGENCIA", "ELETIVO"], [1, 0], inplace = True)
    analysisDB["sexo"].replace(["M", "F"], [0, 1], inplace = True)
    analysisDB["tipo_guia"].replace(["Consulta", "Honorario", "Internacao", "SADT"],["[1,0,0,0]","[0,1,0,0]","[0,0,1,0]","[0,0,0,1]"], inplace = True)
    analysisDB.set_index('id_beneficiario', inplace = True)
    sorted_by_value = analysisDB.sort_values('valor_item', ascending = False)
    classes = [] # Classes de hot encoding para os servicos
    for i in range(size):
        valor = sorted_by_value['valor_item'][i]
        servico = sorted_by_value['servico'][i]
        if valor > 1000 and servico not in classes: # Reserva uma classe para servicos caros
            classes.append(servico)
    frequency = analysisDB.groupby("servico").count().sort_values('sexo', ascending = False)
    limit = size/20
    others = []
    for i in range(frequency.shape[0]):
        num = frequency["sexo"][i]
        servico = frequency.index[i]
        if servico not in classes:
            if num > limit:
                classes.append(servico) # Reserva uma classe para serviços que aparecem em mais de 5% dos casos
            else:
                others.append(servico)

    print("Dados organizados")


    tamanho_hot_encoding = len(classes) + int(bool(others))
    servico_hot_encoding = [str([1 if i == j else 0 for j in range(tamanho_hot_encoding)]) for i in range(tamanho_hot_encoding)]
    analysisDB["servico"].replace(classes, servico_hot_encoding[:tamanho_hot_encoding - 1], inplace = True)
    analysisDB["servico"].replace(others, servico_hot_encoding[-1], inplace = True)

    print("Hot encoding feito")

    lookout_histories = DataFrame(columns = ['history', 'output']) # Pega o histórico de cada paciente crítico
    for i in range(len(analysisDB.values)):
        valor_servico = 0
        line = analysisDB.values[i]
        servico = [value.strip('[,]') for value in line[7].split(' ')]
        for i in range(len(servico)):
            v = servico[i]
            if v == '1':
                valor_servico = i

        carater_atendimento = line[0]
        valor_item = line[1]
        tipo_guia = line[2]
        if carater_atendimento == 0 or (str(valor_item).lower() != 'nan' and int(valor_item) > 1000) or tipo_guia == '[0, 0, 1, 0]':
            id_beneficiario = analysisDB.index[i]
            if lookout_histories.empty or id_beneficiario not in lookout_histories.values[0]:
                hist = get_history(analysisDB, id_beneficiario)
                hist[valor_servico] = 0
                history = DataFrame(index=[0])
                for i in range(len(hist)):
                    history[str(i)] = hist[i]
                history['output'] = valor_servico
                frames = [lookout_histories, history]
                lookout_histories = concat(frames, axis = 0)

    print("DB preparada, entrando no ML")
    lookout_histories.to_csv("lookout_histories.csv")
    # learning(lookout_histories)

main()
