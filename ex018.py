#Faça um programa que leia um angulo qualquer e mostre na tela o valor
#do seno, cosseno e tangente desse angulo.
import math
ang = float(input('Digite um angulo qualquer: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print(f'Para o Angulo de {ang} \n seu Seno é {sen :.2f}'
      f'\n seu Cos é {cos :.2f} e a sua Tangente é {tang :.2f} ')