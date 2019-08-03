# -*- coding:utf-8 -*-
import requests
import datetime

BASIC_URL = 'https://www.btgpactual.com/btgcode/api/'

LISTA_BANCOS = ["banco1","banco2","banco3"]

def calcula_loan(conta):
    headers = {
        'x-api-key': conta,
        'content-type': 'application/json'
    }

    loan_total = 0

    ids_loan = []
    tax_loan = []
    exp_loan = []

    for banco in LISTA_BANCOS:
        url = BASIC_URL + banco + "/loans"
        resp_value = requests.get(url, headers=headers)

        for actual_loan in resp_value.json():
            ids_loan.append(actual_loan["id"])
            tax_loan.append(actual_loan["tax"])
            exp_loan.append(actual_loan['expiryDate'])
            
    for banco in LISTA_BANCOS:
        url = BASIC_URL + banco + '/orders/' + conta
        res_loan = requests.get(url, headers=headers)

        for loan in res_loan.json():
            if ((loan["discriminator"] == "loan") and (loan["idProduto"] in ids_loan)):
                index = ids_loan.index(loan["idProduto"])
                loan_total -= calc_loan(float(loan["valor"]), float(tax_loan[index]), loan["data_ordem"], exp_loan[index])
    
    return str(round(loan_total,2))

def calc_loan(entrada, taxa, data_ord, data_exp):
    now_date = datetime.datetime.today()
    exp_date = datetime.datetime.strptime(data_exp, '%Y-%m-%dT%H:%M:%S.%fZ')

    diff = ((now_date.year - exp_date.year) * 12) + (now_date.month - exp_date.month)
    
    if (diff > 1):
        return 0

    order_date = datetime.datetime.strptime(data_ord, '%Y-%m-%dT%H:%M:%S.%fZ')
    total_ano = (exp_date.year - order_date.year)
    
    return (entrada * ((1 + taxa)**total_ano)) - entrada
