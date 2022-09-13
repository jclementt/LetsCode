nomes_cidades = ['São Paulo', 'Rio de Janeiro', 'Tóquio', 'Paris']
for nome in nomes_cidades:
    print(nome)

cont = 0
nomes_cidades = ['São Paulo', 'Rio de Janeiro', 'Tóquio', 'Paris']
while cont < len(nomes_cidades):
    print(nomes_cidades[cont])
    cont = cont + 1

nomes_cidades = 'São Paulo', 'Rio de Janeiro', 'Tóquio', 'Paris'
for nome in nomes_cidades:
    print(nome)

cidade = {
    'nome': 'RJ',
    'estado': 'RJ',
    'ano': 2022
}
for chave in cidade:
    print(f'{chave}: {cidade[chave]}')

print('----------------------------------------------------')

nomes_cidades = ['São Paulo', 'Rio de Janeiro', 'Tóquio', 'Paris']
for nome in nomes_cidades:
    nome = 'Santos'
print(nomes_cidades)

for posicao in range(len(nomes_cidades)):
    nomes_cidades[posicao] = 'Santos'
print(nomes_cidades)

print('-----------------------------------------------------')

print(list(range(10)))
print(list(range(2, 10)))
print(list(range(2, 10, 2)))
