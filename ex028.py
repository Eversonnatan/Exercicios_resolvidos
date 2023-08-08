#Escreva um programa que faça o computador 'Pensar' em um numero inteiro
#entre 0 e 5 e faça para o usuário  tentar descobri qual foi o numero escolhido
#pelo computador .
# O programa deverá escrever na tela se o usuario venceu ou perdeu.
from random import randint
from time import  sleep
print('Vou Pensar em um Numero entre 0 e 5')
cpu = randint(0, 5)
sleep(4)
print('Pensando............')
joga = int(input('Tente me vencer Mortal: '))
print('Interessante *-*')
sleep(5)
if joga == cpu:
    print(f'Você me venceu que humilhação, eu pensei no numero {cpu}',"*"*20)
else:
    print(f'Você não tem o Q.I Suficiente para esse Jogo !\n Eu pensei no '
          f'numero {cpu}','HAHAHA',"*"*20)

