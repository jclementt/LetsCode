import csv

header = ['nome', 'sobrenome', 'idade']
dados = []
opt = input("""O que deseja fazer?
                [1] -> Cadastrar
                [2] -> Sair\n""")
while opt != '2':
    nome = input('Digite seu nome: ')
    sobrenome = input('Digite seu sobrenome: ')
    idade = input('Digite sua idade: ')
    dados.append([nome, sobrenome, idade])
    opt = input("""O que deseja fazer?
                [1] -> Cadastrar
                [2] -> Sair\n""")
print(dados)

with open('LetsCode/users2.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerows(dados)

with open('LetsCode/users2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)