''''Escreva um programa para aprovar o empréstmo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do
comprador e em quantos anos ele vai pagar. Calcule o valor da prestação
mensal, sabendo que ela não pode exceder 30% do salário ou então o
empréstimo será negado.'''

valor_casa = float(input('Digite o valor da casa desejada:  '))
salario = float(input('Digite o seu salario: '))
anos_pagar = int(input('Em quantos anos deseja pagar o imóvel?  '))
valor_presta = valor_casa/(anos_pagar*12)
limite_empre = (salario*30)/100
if valor_presta >= limite_empre:
    print(f'Para comprar um casa no valor de {valor_casa} em {anos_pagar} anos'
    f' as parcelas seram de R${valor_presta :.2f} \n Empréstimo Negado!!')
else:
    print(f' Para Comprar uma casa no valor de {valor_casa} em {anos_pagar} anos'
    f' as parcelas seram de R${valor_presta:.2f} \n Empréstimo aceito')
