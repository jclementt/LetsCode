# Manipulação de Arquivo

#parâmetros: caminho do arquivo -> modo de abertura (r = read)

#arquivo = open('LetsCode/legiao_urbana.txt', 'r')
#texto = arquivo.read()
#print(texto)
#arquivo.close() #fechar a conexão

#linha = arquivo.readline()
#while linha != '':
#    print(linha, end='')
#    linha = arquivo.readline()
#arquivo.close()  

#arquivo = open('LetsCode/legiao_urbana.txt', 'r')
#for linha in arquivo:
#    print(linha, end='')
#arquivo.close()  

#usa a função close() implicitamente
with open('LetsCode/legiao_urbana.txt', 'r') as arquivo:
    texto = arquivo.read()
    print(texto)

