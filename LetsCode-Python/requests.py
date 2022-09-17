import requests

url = 'https://open.er-api.com/v6/latest'

req = requests.get(url)
print(req.status_code)
dados = req.json()
print(dados)

