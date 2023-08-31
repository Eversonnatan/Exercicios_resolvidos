'''Crie um programa que faça o computador jogar jokenpô com você.'''
print('======= JOKENPÔ ========')
print('[ 1 ] Pedra \n[ 2 ] Papel \n[ 3 ] Tesoura')
jogador = int(input('Qual será sua Jogada:  '))
from time import sleep
from random import randint
sleep(2)
print('JO\nKen\nPô')
sleep(2)
cpu = (randint(1,3))
if cpu == 1 and jogador == 2:
    print('Jogador jogou Papel\njogador Venceu\nComputador jogou Pedra')
elif cpu == 1 and jogador == 3:
    print('Computador jogou Pedra\nComputador venceu\nJogador Jogou Tesoura')
elif cpu == 1 and jogador == 1:
    print('Empate os dois jogaram Pedra')
if cpu == 2 and jogador == 3:
    print('Jogador jogou Tesoura\nJogador venceu\nComputador jogou Papel')
elif cpu == 2 and jogador == 1:
    print('Computador jogou Papel \nComputador venceu\nJogador jogou Pedra')
elif cpu == 2 and jogador == 2:
    print('Empate os dois jogaram Papel')
if cpu == 3 and jogador == 1:
    print('Jogador jogou Pedra\njogador venceu\nComputador jogou Tesoura')
elif cpu == 3  and jogador == 2:
    print('Computador jogou Tesoura\nComputador Venceu\nJogador jogou Papel')
elif cpu == 3 and jogador == 3:
    print('Empate os dois Tesoura')



