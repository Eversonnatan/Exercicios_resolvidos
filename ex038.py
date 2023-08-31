'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior; os dois são iguais
'''

n1 = int(input('Digite o Primeiro valor:  '))
n2 = int(input('Digite o Segundo valor:  '))
if n1 > n2:
    print(f'O primeiro valor é Maior ')
elif n2 > n1:
    print(f'O Segundo valor é Maior')
else:
    print('Os Dois valores são iguais')
