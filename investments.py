# -*- coding:utf-8 -*-
import requests
import datetime

BASIC_URL = 'https://www.btgpactual.com/btgcode/api/'

LISTA_BANCOS = ["banco1","banco2","banco3"]

def calcula_juros(conta):
	headers = {
		'x-api-key': conta,
		'content-type': 'application/json'
	}

	juros_total = 0

	ids_invest = []
	tax_invest = []
	exp_invest = []

	ids_poup = []
	tax_poup = []

	for banco in LISTA_BANCOS:
		url = BASIC_URL + banco + "/investment"
		resp_value = requests.get(url, headers=headers)

		for actual_invest in resp_value.json():
			if (actual_invest["productName"] != "Poupanca"):
				ids_invest.append(actual_invest["id"])
				tax_invest.append(actual_invest["tax"])
				exp_invest.append(actual_invest['expiryDate'])
			else:
				ids_poup.append(actual_invest["id"])
				tax_poup.append(actual_invest["tax"])

	for banco in LISTA_BANCOS:
		url = BASIC_URL + banco + '/orders/' + conta
		res_invest = requests.get(url, headers=headers)

		for invest in res_invest.json():
			if ((invest["discriminator"] == "investment") and (invest["idProduto"] in ids_invest)):
				index = ids_invest.index(invest["idProduto"])
				juros_total += calc_invest(float(invest["valor"]), float(tax_invest[index]), invest["data_ordem"], exp_invest[index])

			elif ((invest["discriminator"] == "investment") and (invest["idProduto"] in ids_poup)):
				juros_total += calc_poupanca(float(invest["valor"]), float(tax_poup[ids_poup.index(invest["idProduto"])]), invest["data_ordem"])
	
	return str(round(juros_total,2))


def calc_poupanca(entrada, taxa, data):
	tax_mes = taxa / 12

	order_date = datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%fZ')
	now_date = datetime.datetime.today()
	total_mes = ((now_date.year - order_date.year) * 12) + (now_date.month - order_date.month)

	return (entrada * ((1 + tax_mes)**total_mes)) - entrada

def calc_invest(entrada, taxa, data_ord, data_exp):
	now_date = datetime.datetime.today()
	exp_date = datetime.datetime.strptime(data_exp, '%Y-%m-%d')

	diff = ((now_date.year - exp_date.year) * 12) + (now_date.month - exp_date.month)
	
	if (diff > 1):
		return 0

	order_date = datetime.datetime.strptime(data_ord, '%Y-%m-%dT%H:%M:%S.%fZ')
	total_ano = (exp_date.year - order_date.year)
	
	return (entrada * ((1 + taxa)**total_ano)) - entrada


#As aplicacoes do tipo poupanca nao serao enviadas
def list_invest(conta):
	all_invest = []

	headers = {
		'x-api-key': conta,
		'content-type': 'application/json'
	}

	for banco in LISTA_BANCOS:
		url = BASIC_URL + banco + "/investment"
		resp_value = requests.get(url, headers=headers)

		for actual_invest in resp_value.json():
			if (actual_invest["productName"] != "Poupanca"):
				temp = actual_invest["expiryDate"][8:]
				temp += "-"
				temp += actual_invest["expiryDate"][5:7]
				temp += "-"
				temp += actual_invest["expiryDate"][0:4]
				actual_invest["expiryDate"] = temp
				
			all_invest.append(actual_invest)
	
	return all_invest
