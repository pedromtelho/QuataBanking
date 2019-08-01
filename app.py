# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for
import requests
from datetime import datetime
import access
import investments as inv
import data
from json import dumps

app = Flask(__name__)

name = ''
amount = 0
account = ''
interest = 0
templateData = {}

@app.route('/', methods=['GET', 'POST'])
def login():
    global name
    global amount
    global account
    global interest
    error = None
    if request.method == 'POST':
        if access.verifica(request.form['privateKey']):
            account = request.form['privateKey']
            name = data.returnName(request.form['privateKey'])
            amount = data.returnBalance(request.form['privateKey'])
            interest = inv.calcula_juros(account)
            return redirect(url_for('home'))  
        else:
            error = 'Chave inválida. Tente novamente.'            
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    global templateData
    balance = amount
    daySpent = 0
    monthTransact = 0
    monthInterest = interest
    day = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    nameClient = name[10:]

    templateData = {
        'balance' : balance,
        'daySpent': daySpent,
        'monthTransact' : monthTransact,
        'name' : nameClient,
        'interest' : monthInterest
    }
    return render_template('home.html', results=templateData)

@app.route('/boleto')
def Boleto():
	return render_template('boleto.html')

@app.route('/transact')
def Transact():
    error = None
    headers = {
        'x-api-key': account
    }
    if request.method == 'POST':
        payload =  {
            "Account": request.form['wallet'],
            "Amount": request.form['value'],
            "Desc": request.form['description']
        }

        data=dumps(payload)

        transf = requests.post('https://www.btgpactual.com/btgcode/api/'+str(access.bank)+'/money-movement/transfer', headers=headers, data=data)
        print(transf.text)
        if transf.text == "Operação realizada com sucesso! $$$":
            return redirect(url_for('home'))
        elif transf.text == "Saldo insuficiente!":
            error = "Saldo insuficiente!"
        else:
            error = 'verifique se as informações contidas no formulário estão corretas.'  
    return render_template('transact.html', error=error, results=templateData)


if __name__ == "__main__":
	app.run(debug=True)