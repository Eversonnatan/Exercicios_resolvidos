#Faça um programa que leia o comprimento do cateto oposto e do cateto
#adjacente de um triangulo retângulo. calcule e mostre o comprimento
#da hipotenusa
'''from math import pow
c_opo = float(input('Digite o Comprimento do cateto oposto: '))
c_adj = float(input('Digite o comprimento do cateto adjacente: '))
soma = (c_opo**2) + (c_adj**2)
hipo =  soma ** (1/2)
print('A hipotenusa do triângulo é {:.2f} '.format(hipo))'''
import math
c_opo = float(input('Digite o Comprimento do cateto oposto: '))
c_adj = float(input('Digite o comprimento do cateto adjacente: '))
hi = math.hypot(c_opo,c_adj)
print(f'O Cateto oposto é {c_opo} \n O cateto adjacente é {c_adj}\n  É a '
      f'Hipotenusa é {hi :.2f}')