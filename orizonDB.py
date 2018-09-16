from pandas import read_csv

def get_DB():
    url = "hackaturing.dsv"
    dtype = {'base_hackaturing.cnpj': str,
            'base_hackaturing.prestador': str,
            'base_hackaturing.uf': str,
            'base_hackaturing.id_beneficiario': str,
            'base_hackaturing.sexo': str,
            'base_hackaturing.data_nascimento': str,
            'base_hackaturing.id_conta': str,
            'base_hackaturing.crm_solicitante': str,
            'base_hackaturing.cbos_solicitante': str,
            'base_hackaturing.cbos_executante': str,
            'base_hackaturing.data_entrada': str,
            'base_hackaturing.data_saida': str,
            'base_hackaturing.data_item': str,
            'base_hackaturing.senha': str,
            'base_hackaturing.tipo_guia': str,
            'base_hackaturing.tipo_item': str,
            'base_hackaturing.carater_atendimento': str,
            'base_hackaturing.servico': str,
            'base_hackaturing.quantidade': float,
            'base_hackaturing.valor_item': float,
            'base_hackaturing.valor_cobrado': float,
            'base_hackaturing.valor_pago': float,
            'base_hackaturing.ano_mes': str,
            'base_hackaturing.cid': str}
    dataset = read_csv(url, sep = '|', dtype = dtype)
    new_columns = [old_name[17:] for old_name in dataset.columns]
    dataset.columns = new_columns
    return dataset

