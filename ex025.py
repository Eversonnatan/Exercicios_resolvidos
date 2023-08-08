# Crie um programa que leia o nome de uma pessoa e
# diga se ela tem "silva" no nome
nome = str(input('Qual é o seu nome Completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))