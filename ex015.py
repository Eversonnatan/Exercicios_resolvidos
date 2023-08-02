#Escreva um programa que pergunte a quantidade de Km percorridos por um
#carro alugado e a quantidade de dias pelos quais ele foi alugado.
#calcule o preço a pagar, sabendo que o carro custa R$60 por dia
#R$0.15 por Km  Rodado.
km = float(input('Digite a quantidade de Km percorridos: '))
dia_alu = int(input('Digite por quantos dias foi alugado o veículo: '))
total = (dia_alu*60) + (km*0.15)
print('Você alugou o carro por {} Dias e percorreu por {}KM \n'
      'O  Total a ser pago será R$ {}'.format(dia_alu,km,total))