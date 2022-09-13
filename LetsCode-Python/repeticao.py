cont = 0
#while cont < 10:
#    cont = cont + 1
#   if cont == 1:
#        print(cont, 'Item Limpo')
#    else:
#        print(cont, 'Itens Limpos')
#print('Fim da repetição do bloco while')

#while True:
#    if cont < 10:
#        cont = cont + 1
#        if cont == 1:
#            print(cont, 'Item Limpo')
#        else:
#            print(cont, 'Itens Limpos')
#    else:
#        break
#print('Fim da repetição do bloco while')

texto = input('Digite a sua senha: ')
while texto != 'LetsCode':
    texto = input('Senha Inválida. Tente novamente: ')
print('Acesso Permitido')