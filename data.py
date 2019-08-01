import requests
import access


def returnName(key):
    lista_bancos = ["banco1","banco2","banco3"]
    for banco in lista_bancos:
        url = "http://www.btgpactual.com/btgcode/api/"+ banco +"/accounts/" + key
        headers = {
            'x-api-key': key
            }
        response = requests.get(url, headers=headers)
        if (response.json()) != "Acesso não encontrado":
            dictionary = response.json()[0]
            name = dictionary['Name']
    return name

def returnBalance(key):
    lista_bancos = ["banco1","banco2","banco3"]
    for banco in lista_bancos:
        url = "http://www.btgpactual.com/btgcode/api/"+ banco +"/accounts/" + key
        headers = {
            'x-api-key': key
            }
        response = requests.get(url, headers=headers)
        if (response.json()) != "Acesso não encontrado":
            dictionary = response.json()[0]
            amount = dictionary['Amount']
    return amount

