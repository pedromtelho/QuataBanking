# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for, Response
import requests
from datetime import datetime
import access
import investments as inv
import data
from json import dumps
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import urllib.request
from os import system, name
from time import sleep 
import auto_invest

app = Flask(__name__)

name = ''
amount = 0
account = ''
interest = 0
templateData = {}
investimento = float()

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
def index():
    return render_template("boleto.html")

@app.route('/Autoinvest', methods=['GET', 'POST'])
def autoinvest():
    global investimento
    error = None
    if request.method == 'POST':
        month = request.form['month']
        uso, investimento = auto_invest.auto_invest(account, month)
        if uso == 0 and investimento == 0:  
            error = 'data inválida. Tente novamente.'
        else:
            return redirect(url_for('Confirmation'))
            # error = 'Este valor será investido'+str(investimento)+'deseja continuar?'
    return render_template("autoinveste.html", error=error, results=templateData)

@app.route('/confirm', methods=['GET', 'POST'])
def Confirmation():
    error = 'Este valor será investido: ' + 'R$' + str(investimento) + '. Deseja realizar o investimento?'
    if request.method == 'POST':
        auto_invest.investe_di(account, str(investimento))
        return redirect(url_for('home'))
        
    return render_template('confirmation.html', results=templateData, error=error)
    


@app.route('/transact', methods=['GET', 'POST'])
def Transact():
    error = None
    headers = {
        'x-api-key': account,
        'content-type': 'application/json'
    }
    if request.method == 'POST':
        data =  {
            "Account": request.form['wallet'],
            "Amount": float(request.form['value']),
            "Desc": request.form['description']
        }

        transf = requests.post('https://www.btgpactual.com/btgcode/api/'+str(access.bank)+'/money-movement/transfer', headers=headers, json=data)
        if transf.text == "\"Operação realizada com sucesso! $$$\"":
            return redirect(url_for('home'))
        elif transf.text == "\"Saldo insuficiente!\"":
            error = "Saldo insuficiente!"
        else:
            error = 'verifique se as informações contidas no formulário estão corretas.'  
    return render_template('transact.html', error=error, results=templateData)

@app.route('/invest')
def Invest():
    #Recebe uma lista com todas as aplicacoes disponiveis em todos os bancos
    #Cada elemento dessa lista é um dicionario contendo uma aplicacao
    list_invest = inv.list_invest(account)

    items = list_invest
        
    # print(list_invest)
    return render_template('investimentos.html',items=items)


if __name__ == "__main__":
    app.run(debug=True)