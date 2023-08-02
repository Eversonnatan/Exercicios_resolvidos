#Escreva um programa que leia um valor em metros e o exiba convertido
#em centimetros e milimetros,km,hm,dam ,m,dm,cm,mm
n = float(input('Digite um valor em metros: '))
cent = n * 100
mili = n * 1000
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
print('O valor digitado foi {}\n seu valor em centimetros {:.2f}cm\n e em milimetros'
      ' {:.2f}mm'.format(n,cent,mili))
print('Em Km {:.3f} , Em Hectometro {} , Em {}Dam , Em {}dm'.format(km,hm,dam,dm))