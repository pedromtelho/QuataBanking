import requests
import datetime

d1 = "2019-06-31T05:33:17"
d2 = '2019-06-30T05:33:17'


data = datetime.datetime.strptime(d2, "%Y-%m-%dT%H:%M:%S")
print(data)

d1 = {"a":1,"b":2}
d2 = {"a":10,"b":2, "c":1}


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

print(merge_dicts(d1, d2))