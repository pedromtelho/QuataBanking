# -*- coding:utf-8 -*-
import requests

def verifica(carteira):
    lista_bancos = ["banco1","banco2","banco3"]
    lista_responses = []
    for banco in lista_bancos:

        url = "http://www.btgpactual.com/btgcode/api/"+ banco +"/accounts/" + carteira

        headers = {
            'x-api-key': carteira
            }

        response = requests.get(url, headers=headers)
        if (response.json()) != "Acesso não encontrado":
            lista_responses.append(response.json()[0])
    if len(lista_responses)>0:
        return True
    else:
        return False