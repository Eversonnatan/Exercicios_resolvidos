#Crie um algoritmo que leia um número e mostre o seu dobro,triplo e a raiz quadrada
n = int(input('Digite um valor: '))
do = n * 2
tri = n * 3
raiz = n ** (1/2)
print('O Número digitado foi {}\n o seu dodro é {} e seu triplo é '
      '{}\n  e sua raiz quadradrada é {:.2f}'.format(n,do,tri,raiz))
