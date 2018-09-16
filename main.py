import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import datetime

import orizonDB

def get_history(analysisDB, id_):
    sexo = analysisDB['sexo'][id_]
    if sexo is not int:
        sexo = sexo.values[0]
    historico = analysisDB.loc[[id_], ['data_item', 'servico', 'carater_atendimento', 'tipo_guia']]
    datas = [datetime.date.fromisoformat(value.split(' ')[0]) for value in historico['data_item']]
    datas.sort()
    if len(datas) == 1:
        media = 0
        mediana = 0
    else:
        delta_datas = []
        for i in range(1, len(datas)):
            delta_datas.append((datas[i] - datas[i-1]).days)

        mediana = delta_datas[len(delta_datas)//2 ]
        media = 0
        for d in delta_datas:
            media += d

        media /= len(delta_datas)
    data_nascimento = analysisDB['data_nascimento']
    if data_nascimento is not datetime.datetime:
        data_nascimento = data_nascimento.values[0]
    idade = (datas[-1]- datetime.date.fromisoformat(data_nascimento)).days
    servicos = historico['servico'].values
    soma_servicos = [0]*len([value.strip('[,]') for value in servicos[0].split(' ')])
    for servico in servicos:
        servico = [value.strip('[,]') for value in servico.split(' ')]
        for i in range(len(servico)):
            soma_servicos[i] += int(servico[i])

    guias = historico['tipo_guia'].values
    soma_guias = [0]*len([value.strip('[]') for value in guias[0].split(',')])
    for guia in guias:
        guia = [value.strip('[]') for value in guia.split(',')]
        for i in range(len(guia)):
            soma_guias[i] += int(guia[i])

    caraters = historico['carater_atendimento'].values
    soma_carater = 0
    for carater in caraters:
        soma_carater += carater

    data = [sexo]+[idade//365]+[media]+[mediana]+soma_guias+[soma_carater]+soma_servicos
    return pandas.DataFrame(data)

def main():
    mainDB = orizonDB.get_DB()
    relevant_columns = ['id_beneficiario',
                        'carater_atendimento',
                        'valor_item',
                        'tipo_guia',
                        'sexo',
                        'data_nascimento',
                        'data_item',
                        'senha',
                        'servico']
    analysisDB = mainDB[relevant_columns][:20000]
    size = analysisDB.shape[0]
    analysisDB["carater_atendimento"].replace(["URGENCIA", "ELETIVO"], [1, 0], inplace = True)
    analysisDB["sexo"].replace(["M", "F"], [0, 1], inplace = True)
    analysisDB["tipo_guia"].replace(["Consulta", "Honorario", "Internacao", "SADT"],["[1,0,0,0]","[0,1,0,0]","[0,0,1,0]","[0,0,0,1]"], inplace = True)
    analysisDB.set_index('id_beneficiario', inplace = True)
    sorted_by_value = analysisDB.sort_values('valor_item', ascending = False)
    classes = []
    for i in range(size):
        valor = sorted_by_value['valor_item'][i]
        servico = sorted_by_value['servico'][i]
        if valor > 1000 and servico not in classes:
            classes.append(servico)
    frequency = analysisDB.groupby("servico").count().sort_values('sexo', ascending = False)
    limit = size/20
    others = []
    for i in range(frequency.shape[0]):
        num = frequency["sexo"][i]
        servico = frequency.index[i]
        if servico not in classes:
            if num > limit:
                classes.append(servico)
            else:
                others.append(servico)


    tamanho_hot_encoding = len(classes) + int(bool(others))
    servico_hot_encoding = [str([1 if i == j else 0 for j in range(tamanho_hot_encoding)]) for i in range(tamanho_hot_encoding)]
    analysisDB["servico"].replace(classes, servico_hot_encoding[:tamanho_hot_encoding - 1], inplace = True)
    analysisDB["servico"].replace(others, servico_hot_encoding[-1], inplace = True)

    lookout_histories = pandas.DataFrame(columns = ['id', 'history', 'output'])
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
                history = get_history(analysisDB, id_beneficiario)
                history[valor_servico] = 0
                line = pandas.DataFrame([[id, history, valor_servico]], columns = ['id', 'history', 'output'])
                lookout_histories.append(line)

    lookout_histories.sort_values('id')

main()
