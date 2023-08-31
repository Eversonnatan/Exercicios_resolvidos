'''Faça um programa que leia o ano de nascimento de um jovem informe, de
acordo com sua idade:*se ele ainda vai se alistar ao serviço militar
*Se é a hora de se alistar. *Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou
do prazo'''
from datetime import date
print('========= Alistamento RedPill ============')
sexo = int(input(' \n[ 1 ] Masculino\n[ 2 ] Feminino\n Informe seu Sexo: '))

if sexo == 1:
  data_nasc = int(input('Informe o ano do nascimento: '))
  ano_atual = date.today().year
  idade = ano_atual - data_nasc
  print(f'Quem nasceu em {data_nasc} tem {idade} anos em {ano_atual}')


if sexo == 1 and idade == 18:
     print('Já está na idade de se Alistar')
elif sexo == 1 and idade > 18:
     passou_lim = idade - 18
     alista = ano_atual - passou_lim
     print(f'Passou da Hora de se Alistar \nVoce deveria ter se '
           f'alistado a {passou_lim} anos  no ano de {alista}')

elif sexo ==1 and  idade < 18:
    no_alist = 18 - idade
    data_aliat = no_alist + ano_atual
    print(f'Ainda falta tempo para se Alistar \nAinda não está '
          f'na Hora De se alistar volte daqui a {no_alist} anos\n'
          f'Volte No ano de {data_aliat}')
elif sexo == 2 :
    print('Mulher não precisa se alistar')
else:
    print('Opção inválida')
