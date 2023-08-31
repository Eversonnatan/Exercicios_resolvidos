''' Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo
Inclusive posso dizer qual tipo de triângulo pode ser formado.
Não deve ser difícil isso em Python.'''
a = float(input('Digite a Primeira reta: '))
b = float(input('Digite a Segunda reta: '))
c = float(input('Digite a terceira reta: '))

if a + b > c and b + c > a and a + c > b:
    print(' Os segmentos acima podem formar um triangulo')
else:
    print(' Não  Pode formar um triangulo ')
