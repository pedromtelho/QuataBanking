import requests
import datetime

def getCardInfo(key):

    dictionary_cartao = {}

    lista_bancos = ["banco1","banco2","banco3"]
    for banco in lista_bancos:

        url = "https://www.btgpactual.com/btgcode/api/"+banco+"/card/"+key

        headers = {
            'x-api-key': "6j7A1fN7buPWINRRD4HY9yo5SnqKAyeUn5W9ZDwq"
            }

        response = requests.request("GET", url, headers=headers)
        if (response.json()) != "Cartão não encontrado":
            dictionary_cartao = response.json()[0]

    return dictionary_cartao        


def getCardFatura(key):

    dictionary_invoice = {}

    lista_bancos = ["banco1","banco2","banco3"]
    for banco in lista_bancos:

        url = "https://www.btgpactual.com/btgcode/api/"+banco+"/card/"+key+"/invoice"

        headers = {
            'x-api-key': "6j7A1fN7buPWINRRD4HY9yo5SnqKAyeUn5W9ZDwq"
            }

        response = requests.request("GET", url, headers=headers)
        if (response.json()) != "Fatura não encontrada":
            dictionary_invoice = response.json()

    return dictionary_invoice


def getFaturaExtrato(key, banco, id):

    url = "https://www.btgpactual.com/btgcode/api/"+banco+"/card/"+key+"/invoice/"+id

    headers = {
        'x-api-key': "6j7A1fN7buPWINRRD4HY9yo5SnqKAyeUn5W9ZDwq"
        }

    response = requests.request("GET", url, headers=headers)
    if (response.json()) != "Fatura não encontrada":
        invoice = response.json()

    return invoice

def gastosTemporaisMes(key,D):
    cartao = getCardInfo(key)
    limite = cartao["CreditLimit"]
    faturas = getCardFatura(key)
    for fatura in faturas:
        data = datetime.datetime.strptime(fatura["CreatedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
        formato = "%Y-%m-%d"
        data = data.strftime(formato)
        if data == D:
            fatura_id = fatura["Id"]
            fatura_banco = fatura["Bank"]
            break

    extrato = getFaturaExtrato(key, fatura_banco, fatura_id)
    dicionario_items = {}
    lista_categorias = []
    for item in extrato:
        lista_categorias.append(item["Desc"])
    for categoria in lista_categorias:
        soma = 0
        for item in extrato:
            if item["Desc"] == categoria:
                soma += item["Amount"]
        dicionario_items[categoria] = soma
    
    return dicionario_items

def gastosTemporaisDia(key,D):
    cartao = getCardInfo(key)
    limite = cartao["CreditLimit"]
    faturas = getCardFatura(key)
    for fatura in faturas:
        data = datetime.datetime.strptime(fatura["CreatedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
        formato = "%Y-%m-%d"
        data = data.strftime(formato)[:7]
        oi = D[:7]
        if data == D[:7]:
            fatura_id = fatura["Id"]
            fatura_banco = fatura["Bank"]
            break

    extrato = getFaturaExtrato(key, fatura_banco, fatura_id)
    dicionario_items = {}
    lista_categorias = []
    for item in extrato:
        lista_categorias.append(item["Desc"])
    for categoria in lista_categorias:
        soma = 0
        for item in extrato:
            data = datetime.datetime.strptime(item["CreatedAt"], "%Y-%m-%dT%H:%M:%S")
            formato = "%Y-%m-%d"
            data = data.strftime(formato)
            if data == D:
                if item["Desc"] == categoria:
                    soma += item["Amount"]
        dicionario_items[categoria] = soma
    
    return dicionario_items







