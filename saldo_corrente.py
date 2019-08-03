import requests
import datetime


def merge_dicts(D1, D2):
    lista1 = list(D1.keys())
    lista2 = list(D2.keys())
    listaf = set(lista1 + lista2)
    df={}
    for categoria in listaf:
        soma = 0
        if categoria in D1:
            soma += D1[categoria]
            df[categoria] = soma
       
        if categoria in D2:
            soma += D2[categoria]
            df[categoria] = soma
    return df



def returnSaldoCorrente(key):
    lista_bancos = ["banco1","banco2","banco3"]
    for banco in lista_bancos:
        url = "http://www.btgpactual.com/btgcode/api/"+ banco +"/money-movement/" + key
        headers = {
            'x-api-key': key
            }
        response = requests.get(url, headers=headers)
        if (response.json()) != []:
            dictionary = response.json()
    return dictionary
#2019-05-31T05:33:17
#2019-05-06T01:06:56
def gastoseparados(key, D):
    faturas = returnSaldoCorrente(key)
    dicionario_items = {}
    lista_categorias = []
    for item in faturas:
        lista_categorias.append(item["Desc"])
    lista_categorias = set(lista_categorias)
    for fatura in faturas:
        tes = fatura["CreatedAt"]
        data = fatura["CreatedAt"]
        #data = datetime.datetime.strptime(fatura["CreatedAt"], "%Y-%m-%dT%H:%M:%S")
        data = data[:10]
        #print(data)

        if data == D or D == "-1":
            #print("Foi")
            for categoria in lista_categorias:
                soma=0
                
                if fatura["Desc"] == categoria:
                    #print(fatura["Desc"])
                    soma += fatura["Amount"]
                    dicionario_items[categoria] = soma
    
    return dicionario_items

def gastoseparadosMes(key, M):
    faturas = returnSaldoCorrente(key)
    dicionario_items = {}
    lista_categorias = []
    for item in faturas:
        lista_categorias.append(item["Desc"])
    lista_categorias = set(lista_categorias)
    for fatura in faturas:
        tes = fatura["CreatedAt"]
        data = fatura["CreatedAt"]
        #data = datetime.datetime.strptime(fatura["CreatedAt"], "%Y-%m-%dT%H:%M:%S")
        data = data[:7]
        #print(data)

        if data == M or M == "-1":
            #print("Foi")
            for categoria in lista_categorias:
                soma=0
                
                if fatura["Desc"] == categoria:
                    #print(fatura["Desc"])
                    soma += fatura["Amount"]
                    dicionario_items[categoria] = soma
    
    return dicionario_items
            
#print(gastoseparados("WAOpEqyHHL6iBASAssi1I63oP4VRxqjqafcJMzYo", "2019-05-06"))

def deltaCorrente(key, Di, Df):
    inicial = gastoseparados(key,Di)
    final = gastoseparados(key,Df)
    delta = merge_dicts(inicial, final)
    return delta

def DictPorct(Di):
    df_n = {}
    df_p = {}
    d_n = {}
    d_p = {}
    for item in Di.items():
        if item[1] < 0:
            d_n[item[0]] = item[1]
        else:
            d_p[item[0]] = item[1]

    total_p = sum(d_p.values())
    total_n = sum(d_n.values())
    for categorias in d_p.items():
        df_p[categorias[0]] = categorias[1]/total_p

    for categorias in d_n.items():
        df_n[categorias[0]] = categorias[1]/total_n

    return df_n, df_p

def separa_income(Di):
    d_n = {}
    d_p = {}
    for item in Di.items():
        if item[1] < 0:
            d_n[item[0]] = item[1]
        else:
            d_p[item[0]] = item[1]

    return d_p, d_n

print((gastoseparadosMes("WAOpEqyHHL6iBASAssi1I63oP4VRxqjqafcJMzYo", "2019-06")))