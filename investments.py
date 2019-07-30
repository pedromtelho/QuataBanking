# -*- coding:utf-8 -*-
import requests

BASIC_URL = 'http://www.btgpactual.com/btgcode/api/'

def calcula_juros(conta):
	conta = 'X6XPMTOUOvmh4xzKHvbS6OKLPEYMHEh985pcHJD0'
	juros_total = 0
	lista_bancos = ["banco1","banco2","banco3"]

	for banco in lista_bancos:
		url = BASIC_URL + banco + '/orders/' + conta
		headers = {
			'x-api-key': conta,
			'content-type': 'application/json'
		}
		res_invest = requests.get(url, headers=headers)

		for invest in res_invest.json():
			if (invest["discriminator"] == "investment"):
				url = BASIC_URL + banco + "/investment"
				resp_value = requests.get(url, headers=headers)
				for actual_invest in resp_value.json():
					if (actual_invest["id"] == invest["idProduto"]):
						print(actual_invest["tax"])
						print(invest["valor"])
						juros_total += float(invest["valor"]) * float(actual_invest["tax"])

	return str(juros_total)