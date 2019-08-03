import saldo_corrente as saldos



#[['Chrome', 58.9], ["oi", 30]]
"2019-06"

def DictPorct(Di):
    d_n = {}
    total_n = sum(Di.values())

    for categorias in Di.items():
        d_n[categorias[0]] = str(round((100*categorias[1]/total_n),2))

    return d_n


def pie(key, mes):
    d_p, d_n = saldos.separa_income(saldos.gastoseparadosMes(key, mes))
    d_o = DictPorct(d_n)
    array = []
    for item in d_o.items():
        array.append([item[0],float(item[1])])
    return array


print(pie("WAOpEqyHHL6iBASAssi1I63oP4VRxqjqafcJMzYo" ,"2019-06"))
