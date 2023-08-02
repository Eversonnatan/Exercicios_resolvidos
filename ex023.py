#Faça um programa que leia um Número de 0 a 9999 e mostre na tela cada
#um dos digitos separados , ex:Digite um numero: 1834
#unidade: 4  dezena:3  centena:8  milhar:1
n = (input('Digite um numero de 0 a 9999: '))
uni = len(n)
print(f'unidade:{n[3]} ')
print(f'a Dezena:{n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')
