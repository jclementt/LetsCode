#def calcula_media(valor1, valor2, valor3):
#    soma = valor1 + valor2 + valor3
#    media = soma / 3
#    return media

def calcula_media(*args):
    soma = sum(args)
    media = soma / len(args)
    return media

print(calcula_media(10, 9, 10))

print('-----------------------------------------------')

def print_info(**kwargs):
    print(kwargs, type(kwargs))

print_info(nome='Joanna', sobrenome='Clementino')
