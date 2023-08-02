#O mesmo professor do desafio anterior quer sortear a ordem de apresentação
#de trabalhos dos alunos. Faça um programa que leia o nome dos  quatros
#alunos e mostre a ordem sorteada.
from random import  shuffle
al_1 = str(input('Digite o nome do 1º aluno: '))
a_2  = str(input('Digite o nome do 2º aluno: '))
al_3 = str(input('Digite o nome do 3º aluno: '))
al_4 = str(input('Digite o nomr do 4° aluno: '))
ordem = [al_1,a_2,al_3,al_4]
shuffle(ordem)
print('A ordem de apresentação será ')
print(ordem)
