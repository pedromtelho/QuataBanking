# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for
import requests
import datetime
import access
import investments as inv
import data
from json import dumps
import saldo_corrente as saldos
import auto_invest
import boleto as bo

app = Flask(__name__)

name = ''
amount = 0
account = ''
interest = 0
templateData = {}
investimento = float()

def DictPorcte(Di):
    d_n = {}
    total_n = sum(Di.values())

    for categorias in Di.items():
        d_n[categorias[0]] = str(round((100*categorias[1]/total_n),2))

    return d_n


def pie(key, mes):
    d_p, d_n = saldos.separa_income(saldos.gastoseparadosMes(key, mes))
    d_o = DictPorcte(d_n)
    array = []
    for item in d_o.items():
        array.append([item[0],float(item[1])])
    return array


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
    day = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    nameClient = name[10:]

    now = datetime.datetime.today()
    if (now.month == 1):
        dataUse = str(now.year-1)+"-12"
    elif (len(str(now.month-1)) == 1):
        dateUse = str(now.year)+"-0"+str(now.month-1)
    else:
        dateUse = str(now.year)+"-"+str(now.month-1)

    dateUse = "2019-08"
    pMonthNeg, pMonthPlus = saldos.DictPorct(saldos.gastoseparadosMes(account,dateUse))

    chartData = index()
    #print("PAU NO SEU CU: " + str(index()))
    templateData = {
        'balance' : balance,
        'daySpent': daySpent,
        'monthTransact' : monthTransact,
        'name' : nameClient,
        'interest' : monthInterest,
        'chart': chartData
    }
    
    return render_template('home.html', entradas=pMonthPlus, saidas=pMonthNeg, results=templateData)

def index(chartID = 'chart_ID', chart_type = 'pie', chart_height = 350):
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": pie(account, "2019-06")}]
    title = {"text": 'Gasto'}
    xAxis = {"categories": list(saldos.gastoseparadosMes(account,"2019-06").keys())}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return { "chartID": 'expensesChart' , "chart": chart, "series": series, "title": title, "xAxis": xAxis, "yAxis": yAxis}

@app.route('/boleto', methods=['GET','POST'])
def Boleto():
    status = None
    if request.method == 'POST':
        status = bo.pagaBoleto(account, float(request.form['value']), request.form['description'])
    if status == True:
        error = "Sucesso!"
    else:
        error = "Confira o formulario"
    return render_template('boleto.html', status = error, results=templateData)

@app.route('/extrato')
def Extrato():
    dictExtract = saldos.list_all_extract(account)
    return render_template('extract.html', dictExtract=dictExtract, results=templateData)

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


@app.route('/invest')
def Invest():
    #Recebe uma lista com todas as aplicacoes disponiveis em todos os bancos
    #Cada elemento dessa lista é um dicionario contendo uma aplicacao
    list_invest = inv.list_invest(account)

    items = list_invest
        
    # print(list_invest)
    return render_template('investimentos.html',items=items, results=templateData)


if __name__ == "__main__":
    app.run(debug=True)