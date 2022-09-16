# Manipulação de Arquivo
print('-=' * 20)

with open('LetsCode/arquivo_teste.txt', 'w') as arquivo:
    arquivo.write('Primeira Linha de Teste - Python\n')
    arquivo.write('Segunda Linha de Teste - Python\n')

with open('LetsCode/arquivo_teste.txt', 'r') as arquivo:
    print(arquivo.read(), end='')

with open('LetsCode/arquivo_teste.txt', 'a') as arquivo:
    arquivo.write('Terceira Linha de Teste - Python\n')

print('-=' * 20)

with open('LetsCode/arquivo_teste.txt', 'r') as arquivo:
    print(arquivo.read(), end='')

# r+ combina w e r
print('-=' * 20)
