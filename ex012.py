#Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço com 5% de desconto.
prod = float(input('Digite o preço do produto: '))
novo_pre = prod - (prod * 5)/100

print('O Produto que custava {:.2f},\n na promoção com desconto ded 5% '
      'vai custar R${:.2f}'.format(prod,novo_pre))