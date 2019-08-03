import saldo_corrente as sd
import datetime
from dateutil.relativedelta import *

def operando_mes(data, n):
    date_time_obj = datetime.datetime.strptime(data, '%Y-%m')
    use_date = str(date_time_obj + relativedelta(months=+n))
    return use_date[:7]



def detecta_media(key, mes):
    primeiro_mes = sd.gastoseparadosMes(key, mes)
    mes_anterior = operando_mes(mes,-1)
    segundo_mes = sd.gastoseparadosMes(key, mes_anterior)
    d_p1, d_n1 = sd.separa_income(primeiro_mes)
    d_p2, d_n2 = sd.separa_income(segundo_mes)
    negativo = sd.merge_dicts(d_n1, d_n2)
    positivo = sd.merge_dicts(d_p1, d_p2)
    negativo = sum(negativo.values())/2
    positivo = sum(positivo.values())/2
    return positivo, negativo

def valor_a_ser_investido(positivo, negativo, porc):
    saldo = positivo - negativo
    investimento = saldo*porc
    uso = saldo - investimento

    return uso, investimento



positivo, negativo = detecta_media("piDcR48aYV4L9EmhDECLN4eQGeKJsZ8312laCf6b", "2019-06")
print(valor_a_ser_investido(positivo, negativo, 0.3))