# -*- coding:utf-8 -*-
import requests

BASIC_URL = 'https://www.btgpactual.com/btgcode/api/'


def calcula_juros(conta):
	headers = {
		'x-api-key': conta,
		'content-type': 'application/json'
	}

	juros_total = 0
	lista_bancos = ["banco1","banco2","banco3"]

	ids_invest = []
	tax_invest = []

	for banco in lista_bancos:
		url = BASIC_URL + banco + "/investment"
		resp_value = requests.get(url, headers=headers)

		for actual_invest in resp_value.json():
			ids_invest.append(actual_invest["id"])
			tax_invest.append(actual_invest["tax"])

	for banco in lista_bancos:
		url = BASIC_URL + banco + '/orders/' + conta
		res_invest = requests.get(url, headers=headers)

		for invest in res_invest.json():
			if ((invest["discriminator"] == "investment") and (invest["idProduto"] in ids_invest)):
				juros_total += float(invest["valor"]) * float(tax_invest[ids_invest.index(invest["idProduto"])])
				
	return str(juros_total)
