import requests

#tia nana
#carteira = "WAOpEqyHHL6iBASAssi1I63oP4VRxqjqafcJMzYo"
#Joao Hancok
#carteira = "piDcR48aYV4L9EmhDECLN4eQGeKJsZ8312laCf6b"
#Junior
carteira = "tuERPHixmI55KR0sEm32n1AF72mq1rJnaubqamc1"


def conta(carteira):
    lista_bancos = ["banco1","banco2","banco3"]
    lista_responses = []
    for banco in lista_bancos:

        url = "http://www.btgpactual.com/btgcode/api/"+ banco +"/loans/"

        headers = {
            'x-api-key': carteira
            }

        response = requests.request("GET", url, headers=headers)
        if len(response.json()) > 0:
            lista_responses.append(response.json()[0])

    return lista_responses

print(conta(carteira))