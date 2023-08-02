#Faça um programa que leia algo pelo tecido e mostre na tela o se tipo
#primitivo e todos as informações possiveis
n = input('Digite Algo e vejs as informações: ')
print('O seu Tipo Primitivo é: ',type(n))
print('É numerico: ',(n.isnumeric()))
print('É Decimal: ',n.isdecimal())
print('É alfabético: ',n.isalpha())
print('Esta Capitalizada: ',n.istitle())
print('Está em Minusculo: ',n.islower())
print('Está em Maiusculo: ',n.isupper())
print('So tem espaços: ',n.isspace())
print('É Alfanúmerico: ',n.isalnum())
