#crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dolares ela pode comprar. Considere  Us$1.00 = 3.27
cart = float(input('Digite o tanto de dinheiro que tem na carteira R$: '))
Conve = cart / 3.27
print('Com {} voce pode comprar U${:.2f}'.format(cart,Conve))