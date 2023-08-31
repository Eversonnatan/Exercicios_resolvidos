'''Refaça o desafio 035 dos triangulos,acrescentando o recurso de mostrar
que tip de triângulo será formado:
*Equilátero:todos os lados iguais , *Isósceles:dois lados iguais
*Escaleno:todos os lados diferentes'''
a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: ' ))

if a + b > c and b + c > a and a + c > b:
    print('Os Segmentos acima podem gerar um triangulo ', end='')
    if a != b and b != c and a != c:
        print('Escaleno')
    elif a == b and a == c and b == c:
        print('Equilátero')
    else:
        print('Isósceles')
else:
    print('Os segmentos não podem formar um triangulo')



