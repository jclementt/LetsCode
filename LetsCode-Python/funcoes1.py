from statistics import median


def hello():
    print('Olá Mundo!')

hello()

def calcula_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

resultado = calcula_media(9, 8, 10)
print(resultado)

resultado2 = calcula_media(9, 10, 9)
print(resultado2)

print('Olá,', end=' ')
print('Dafne')

def calcula_media(valor1=0, valor2=0, valor3=0):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

resultado3 = calcula_media()
print(resultado3)
