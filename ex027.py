#Faça um programa que leia o nome completo de uma pessoa.
#mostre em seguida o primeiro e o ultimo nome separadamente
#Ex: Ana maria de Souza  //Primeiro=Ana , Último=Souza
nome = str(input('digite seu nome completo: '))
pri_nome = nome.split()
print('Primeiro: ',pri_nome[0])
print('Último: ' , pri_nome[-1])
