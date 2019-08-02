import requests
import datetime


def merge_dicts(D1, D2):
    lista1 = list(D1.keys())
    lista2 = list(D2.keys())
    listaf = set(lista1 + lista2)
    df={}
    for categoria in listaf:
        soma = 0
        for e in D1:
            if categoria in D1:
                soma += D1[categoria]
                df[categoria] = soma
        for e in D2:
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
        print(data)

        if data == D or D == "-1":
            print("Foi")
            for categoria in lista_categorias:
                soma=0
                
                if fatura["Desc"] == categoria:
                    print(fatura["Desc"])
                    soma += fatura["Amount"]
                    dicionario_items[categoria] = soma
    
    return dicionario_items
            
#print(gastoseparados("WAOpEqyHHL6iBASAssi1I63oP4VRxqjqafcJMzYo", "2019-05-06"))

def deltaCorrente(key, Di, Df):
    inicial = gastoseparados(key,Di)
    final = gastoseparados(key,Df)
    delta = merge_dicts(inicial, final)
    return delta

