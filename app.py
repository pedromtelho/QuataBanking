# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for
# from QRreader import *
import requests
from datetime import datetime
import access 
import investments as inv

app = Flask(__name__)
# url = "https://www.btgpactual.com/btgcode/api/money-movement"

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if access.verifica(request.form['privateKey']):
			return redirect(url_for('home'))        
		else:
			error = 'Chave inválida. Tente novamente.'            
	return render_template('login.html', error=error)

@app.route('/home')
def home():
	balance = 10000
	daySpent = 0
	monthTransact = 0
	day = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	templateData = {
		'balance' : balance,
		'daySpent': daySpent,
		'monthTransact' : monthTransact
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

@app.route('/juros')
def Juros():
	total = inv.calcula_juros()
	return total


if __name__ == "__main__":
	app.run(debug=True)