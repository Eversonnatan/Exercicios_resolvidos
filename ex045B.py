#Jokenpo
from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
cpu = randint(0,2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador !=2:
    print('Opção errada\nTente Novamente! ')
else:
 print('Jo')
 sleep(1)
 print('ken')
 sleep(1)
 print('Po!!!')
 print('-='*11)
 print(f'Skynet jogou {itens[cpu]}')
 print(f'Jogador jogou {itens[jogador]}')
 print('-='*11)
if cpu == 0: # cpu jogou pedra
    if jogador == 0:
     print('Empate')
    elif jogador == 1:
     print('Jogador Venceu')
    elif jogador == 2:
     print('Skynet Venceu')
    else:
        print('Jogada Inválida')
elif cpu == 1: # cpu jogou Papel
    if jogador == 0:
        print('Skynet Venceu')
    elif jogador == 1:
       print('Empate')
    elif jogador == 2:
        print('Jogador Venceu')
    else:
        print('Jogada Inválida')
elif cpu == 2: # cpu jogou tesoura
    if jogador == 0:
     print('Jogador Venceu')
    elif jogador == 1:
        print('skynet Venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogador Inválida')
