'''Escreva um programa que pergunte o salário de um
funcionário e calcule o valor do seu aumento
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de R$ 15%.'''
salario = float(input('Digite o salario do Funcionario: '))
aument_1 = (salario+(salario*10)/100)
aument_2 = (salario+(salario*15)/100)
if salario >= 1250:
    print(f'O seu aumento será de 10% , salario final { aument_1:.2f}')
else:
    print(f'O seu aumento será de 15% , salário final { aument_2:.2f}')
