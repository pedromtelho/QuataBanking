# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for
import requests
from datetime import datetime
import access
import investments as inv
import data

app = Flask(__name__)

name = ''
amount = 0
account = ''
interest = 0



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
	return render_template('transact.html')



if __name__ == "__main__":
	app.run(debug=True)