#Faça um programa que leia a largura e a altura de uma parede em metros.
#Calcule a sua área e a quantidade da tinta necesário para pintá-la,
#sabendo que cada litro, de tinta pinta uma área de 2m2
larg = float(input('Digite a Largura da parede: '))
alt = float(input('Digite a Altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}mº'.format(larg,alt,area))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))