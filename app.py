from flask import Flask, request, render_template, redirect, url_for
import requests
from datetime import datetime
import access 
import data

app = Flask(__name__)

name = ''
amount = 0
account = ''


@app.route('/', methods=['GET', 'POST'])
def login():
    global name
    global amount
    global account
    error = None
    if request.method == 'POST':
        if access.verifica(request.form['privateKey']):
            account = request.form['privateKey']
            name = data.returnName(request.form['privateKey'])
            amount = data.returnBalance(request.form['privateKey'])
            return redirect(url_for('home'))  
        else:
            error = 'Chave inválida. Tente novamente.'            
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    balance = amount
    daySpent = 0
    monthTransact = 0
    day = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    nameClient = name[10:]


    templateData = {
        'balance' : balance,
        'daySpent': daySpent,
        'monthTransact' : monthTransact,
        'name' : nameClient
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