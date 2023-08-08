#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h, mostre uma mensagem
#dizendo que ele foi multado
#A multa vai custar R$7,00 por cada Km acima do limite.
velo = float(input('Digite a velocidade do carro: '))
multa = 7*(velo - 80)
if velo > 80:
    print(f'Você Ultrapassou a velocidade permitida , será Multado em {multa:.1f}R$!')

else:
    print('Velocidade Dentro do Limite. Boa Viagem')

