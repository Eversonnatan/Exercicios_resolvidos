# Crie um programa que leia o nome de uma pessoa e
# diga se ela tem "silva" no nome
print(18*"-")
nome = str(input('Digite o seu nome:  ')).strip().title()
print('Analisando seu nome', 10*'.')
if 'Silva' in nome:
    print('O seu nome Possui Silva')
else:
    print('Seu nome não tem silva')