#Faça um algoritmo que leia o salário de um funcionário e mostre seu
#novo salário, com 15 % de aumento.
sala = float(input('Digite o salário do Funcionário:  '))
Novsal = sala + (sala*15)/100
print('O Salário antigo do funcionário é R${:.2f} \n e com aumento de '
      '15% fica R${:.2f}'.format(sala,Novsal))