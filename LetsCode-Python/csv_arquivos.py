import csv

#leitura
with open('LetsCode/aluno.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    header = next(leitor)
    for linha in leitor:
        if float(linha[2]) >= 18:
            print(linha)

#escrita
# newline='' (faz com que o python não pule um alinha após o header)
with open('LetsCode/users.csv', 'w', newline='') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['Joanna', 'Clementino', 'joanna@gmail.com', 'Feminino'])


