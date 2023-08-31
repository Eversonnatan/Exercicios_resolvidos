''' Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
2 para hexadecimal
'''
n = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para a conversão: '
      '\n[ 1 ] converter para BINÁRIO \n[ 2 ] converter para OCTAL '
      '\n[ 3 ] conveter para HEXADECIMAL')
op = int(input('Sua opção: '))
if op == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif op == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]} ')
elif op == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print('Opção inválida \nTente Novamente')