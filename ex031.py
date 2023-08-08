'''Desenvolva um programa que pergunte a distância
de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50
por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas'''
dist = float(input('Digite a distância da viagem em Km: '))
ate_200 = 0.50 * dist
pas_200 = 0.45 * dist
if dist <= 200:
    print(f'A viagem irá custar R$ {ate_200:.2f}')
else :
    print(f'A viagem irá custar R$ {pas_200 :.2f}')