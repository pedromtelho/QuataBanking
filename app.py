from flask import Flask, request, render_template
# from QRreader import *
import requests
from datetime import datetime


key = "WAOpEqyHHL6iBASAssi1I63oP4VRxqjqafcJMzYo"
app = Flask(__name__)
url = "https://www.btgpactual.com/btgcode/api/money-movement"

def conta(carteira):
    lista_bancos = ["banco1","banco2","banco3"]
    lista_responses = []
    for banco in lista_bancos:

        url = "http://www.btgpactual.com/btgcode/api/"+ banco +"/accounts/"+ carteira

        headers = {
            'x-api-key': carteira
            }

        response = requests.request("GET", url, headers=headers)
        if response.json() != "Acesso não encontrado":
            lista_responses.append(response.json()[0])

    return lista_responses

def pega_dados(lista_js):
    for e in lista_js:
        banco = e.get("Bank")
        soma = e.get("Amount")
        nome = e.get("Name")
    return banco, soma, nome

@app.route('/')
def mainpage():
    global key
    lista_bancos = conta(key)
    banco, balance,nome = pega_dados(lista_bancos)
    monthTransact = 0
    day = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    templateData = {
			'balance' : balance,
            'daySpent': 0,
            'monthTransact' : 0,
            'nome': nome
    }
    return render_template('home.html', results=templateData)


# @app.route('/extract', methods=['GET'])
# def Extract():

#     resultDesc = []
#     resultAmount = []
#     resultCPart = []
#     resultData = []

#     headers = {
#     "x-api-key": "6j7A1fN7buPWINRRD4HY9yo5SnqKAyeUn5W9ZDwq"
#     }
#     r = requests.get('https://www.btgpactual.com/btgcode/api/money-movement', headers=headers)
#     listJson = r.json()


#     for j in listJson:
#         for i, k in j.items():
#             if i == "Desc":
#                 resultDesc.append(str(k))
#             if i == "Amount":
#                 resultAmount.append(str(k))
#             if i == "Counterpart":
#                 resultCPart.append(str(k))
#             if i == "CreatedAt":
#                 resultData.append(str(k[8:10] + k[4:8] + k[0:4]))
#         extract = {
#             'wallet' : resultCPart,
# 			'desc' : resultDesc,
#             'data': resultData,
#             'value' : resultAmount
#         }

#     return render_template('extract.html', extract=extract)

@app.route('/boleto')
def Boleto():
    return render_template('boleto.html')

@app.route('/transact')
def Transact():
    return render_template('transact.html')


if __name__ == "__main__":
    app.run(debug=True)