import requests

url = "https://www.btgpactual.com/btgcode/api/banco3/orders/tuERPHixmI55KR0sEm32n1AF72mq1rJnaubqamc1"

payload = " {\r\n   \"IdProduct\": \"4882b6d1-e24f-4dab-924e-4428a7c93f14\",\r\n   \"AcquisitionDate\": \"2018-06-05\",\r\n   \"Amount\": 150\r\n   \r\n}"
headers = {
    'Content-Type': "application/json",
    'x-api-key': "6j7A1fN7buPWINRRD4HY9yo5SnqKAyeUn5W9ZDwq",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "9c98caec-fa9d-4d99-8740-95bf82978e07,21100705-d756-4f8a-8edd-a3f20653894c",
    'Host': "www.btgpactual.com",
    'cookie': "visid_incap_1245163=Im8rdfK5RtihO1lewIezkeIKNl0AAAAAQUIPAAAAAAAngTsO39FfiT6TgkTxsh8b; nlbi_1245163=YAiVCmx+lACv682T3WZq6wAAAAC8MeaUoiasNN5IBcOEzDvP; incap_ses_785_1245163=yK7NDNp+MyCArwDDS+LkCq9gP10AAAAAC6S3Iuj13kuraMv26gg1JQ==; incap_ses_1242_1245163=Yv5oMRNAhyNS9pdMqng8EYPQRF0AAAAAojmZHVxH+uCHN/1jES7bPQ==; AWSELB=B9835DAEE4B62A9E87CF2862EFB8C3D10B0BE4FF73FA83FC13538F998D9A7C456BE319FC8909B29E3D976CD9E39C555D8BA9F5AF4B3654C36D9020AAE7A37F3CF68A10D9",
    'accept-encoding': "gzip, deflate",
    'content-length': "122",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)