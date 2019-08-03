import requests

def pagaBoleto(key, ammount, desc):

    lista_bancos = ["banco1","banco2","banco3"]
    for banco in lista_bancos:
        url = "https://www.btgpactual.com/btgcode/api/"+banco+"/money-movement/pay"
        payload = "{\n    \"Account\": \""+key+"\",\n    \"Amount\": "+str(ammount)+",\n    \"Desc\": \""+desc+"\"\n}"
        headers = {
        'Content-Type': "application/json",
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        if (response.json()) != "Saldo insuficiente!":
            return True
        
        else:
            return False

