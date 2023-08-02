#Crie um programa  que leia o nome de uma cidade e
#diga se ela começa ou não com o nome "Santo"
cidade = str(input('Digite o nome da sua Cidade: ')).capitalize().strip()
ver = cidade.split()
if ver[0] == 'Santo':
    print('A sua Cidade começa com Santo')
else:
    print('Sua Cidade não começa com Santo')
