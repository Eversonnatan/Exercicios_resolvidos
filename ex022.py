#Crie um programa que leia o nome completo de uma pessoa e, mostre:
#O nome com todas as letras maiusculas
#o nome com todas minusculas
#Quantas letras ao tod (sem considerar espaços)
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome: ')).strip()
print(nome.upper())
print(nome.lower())
print('O nome {} possui o total de letras {}.'.format(nome,len(nome) - nome.count(' ')))
#print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print(('Seu primeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0]))))


