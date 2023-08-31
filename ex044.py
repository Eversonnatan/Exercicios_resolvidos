'''Elabora um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:
*á vista dinheiro/cheque: 10% de  desconto , *em até 2x no cartão:preço normal
*á vista no cartão:5% de desconto , *3x ou mais no cartão:20%de juros'''
print('============ LOJAS RED PILL ==============')
preco = float(input('Preço das Compras: '))
print('FORMAS DE PAGAMENTO \n[ 1 ]á vista dinheiro/cheque\n[ 2 ]á vista cartão '
      '\n[ 3 ] 2x no cartão \n[ 4 ] 3x ou mais no cartão ')
op = int(input('Qual é a opção:  '))
if op == 1:
    vista = preco - (preco * 10 / 100)
    print(f'Sua compra a vista no dinheiro foi de R$ {preco:.2f} e'
          f' com 10% de desconto ficou R$ {vista:.2f}')
elif op == 2:
    cart_vist = preco - (preco * 5 / 100)
    print(f'Sua compra a vista no cartão foi de R$ {preco:.2f} e'
          f' com 5% de desconto ficou R$ {cart_vist:.2f}')
elif op == 3:
    parc = preco / 2
    print(f'Sua compra de  R${preco} \nserá parcelada em 2x de {parc} sem Juros')

elif op == 4:
    qt_par = int(input('Em quantas vezes será o pagamento? '))
    valo_juro = preco+(preco*20/100)
    parc_juro = valo_juro/qt_par
    print(f'Sua compra sera parcelada em {qt_par}x de {parc_juro:.2f} COM JUROS\n'
    f'Sua compra de R$ {preco:.2f} vai custar {valo_juro:.2f} no final')
else:
    print(f'Sua compra foi de R${preco}'
          '\nOpção inválida\nTente Novamente!!')

