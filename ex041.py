'''A Confederação nacional de natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria de acordo com a idade:
* Até 9 anos:Mirim , *Até 14 anos:Infantil , Até 19 anos:Junior
*Até 25 anos:Sénior , *Acima:Master'''
from datetime import date
data_nasc = int(input('Digite a data do Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - data_nasc
if idade <= 9:
    print(f'Com a idade de {idade} anos \nsua classificação é Mirim')
elif idade <= 14:
    print(f'Com a idade de {idade} anos \nSua classificação é Infantil')
elif idade <= 19:
    print(f'Com a idade de {idade} anos \nSua classificação é Junior')
elif idade <= 25:
    print(f'Com a idade de {idade} anos \nSua classificação é Sénior')
else:
    print(f'Com a idade de {idade} anos \nSua classificação é Master')
