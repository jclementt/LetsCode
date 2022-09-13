dados_cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'area_km': 1521,
    'populacao': 12.12,
}

print(type(dados_cidade))
print(dados_cidade)

dados_cidade['pais'] = 'Brasil'
print(dados_cidade)

dados_cidade['area_km'] = 1500
print(dados_cidade)

dados_cidade2 = dados_cidade
dados_cidade2['nome'] = 'Santos'
print(dados_cidade)
print(dados_cidade2)

dados_cidade3 = dados_cidade.copy()
dados_cidade3['populacao'] = 10.58
print(dados_cidade)
print(dados_cidade3)

novos_dados = {
    'populacao': 6.7,
    'independencia': '07/09/1822',
    'nome': 'Cidade Maravilhosa',
    'estado': 'Rio de janeiro',
    'area_km': 1.200
}

dados_cidade.update(novos_dados)
print("Atuaização: ", dados_cidade)

print(dados_cidade.get('Joanna'))

print(dados_cidade.keys()) # retorna a lista de chaves de um dicionário
print(dados_cidade.values()) # retorna uma lista de valores de um dicionário
print(dados_cidade.items()) # retorna uma lista de tuplas (chave, valor) de um dicionário
