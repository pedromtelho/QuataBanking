import requests

url = "http://www.btgpactual.com/btgcode/api/banco3/money-movement"

payload = "{\r\n    \"Account\": \"WAOpEqyHHL6iBASAssi1I63oP4VRxqjqafcJMzYo\",\r\n    \"Amount\": 4,\r\n    \"Counterpart\": \"tuERPHixmI55KR0sEm32n1AF72mq1rJnaubqamc1\",\r\n    \"Desc\": \"Teste\"\r\n }"
headers = {
    'x-api-key': "6j7A1fN7buPWINRRD4HY9yo5SnqKAyeUn5W9ZDwq",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)