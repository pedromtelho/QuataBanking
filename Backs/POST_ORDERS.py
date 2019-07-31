import requests

url = "http://www.btgpactual.com/btgcode/api/banco1/orders/tuERPHixmI55KR0sEm32n1AF72mq1rJnaubqamc1"

payload = "{\r\n   \"Account\": \"tuERPHixmI55KR0sEm32n1AF72mq1rJnaubqamc1\",\r\n   \"CounterPartAccount\": \"piDcR48aYV4L9EmhDECLN4eQGeKJsZ8312laCf6b\",\r\n   \"IdProduct\": \"dd18b2ad-756c-4157-b3ee-802d2da2cd05\",\r\n   \"AcquisitionDate\": \"2019-23-07\",\r\n   \"Amount\": 50\r\n}"
headers = {
    'Content-Type': "application/json",
    'x-api-key': "tuERPHixmI55KR0sEm32n1AF72mq1rJnaubqamc1",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "ad40835a-8aab-441b-ad3a-bf1caf73d1cf,e829fd31-a7e1-48f9-a3da-b69a5a4e9063",
    'cookie': "visid_incap_1245163=Im8rdfK5RtihO1lewIezkeIKNl0AAAAAQUIPAAAAAAAngTsO39FfiT6TgkTxsh8b; nlbi_1245163=YAiVCmx+lACv682T3WZq6wAAAAC8MeaUoiasNN5IBcOEzDvP; incap_ses_785_1245163=h2uHA1c9d1Z8JPq9S+LkCgxAN10AAAAAgUTtplD1YPQRK8/yh3reGQ==; incap_ses_787_1245163=u2RnLsSG3FoxBatTWf3rCs4QN10AAAAAoBZpvhyNYo3UzYTiZikLiA==; AWSELB=B9835DAEE4B62A9E87CF2862EFB8C3D10B0BE4FF73FA83FC13538F998D9A7C456BE319FC8909B29E3D976CD9E39C555D8BA9F5AF4B3654C36D9020AAE7A37F3CF68A10D9",
    'accept-encoding': "gzip, deflate",
    'referer': "http://www.btgpactual.com/btgcode/api/banco1/orders/tuERPHixmI55KR0sEm32n1AF72mq1rJnaubqamc1",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response)