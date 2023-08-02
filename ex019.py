# Um Professor quer sortear um dos seus quatros alunos para apagar
#o quadro. Faça um programa que ajude ele , lendo o nome deles e
#escrevendo o nome do escolhido.
from random import choice
print('Professor: Vou escolher quem, vai apagar o Quadro negro  ')
alu_1 = str(input('Digite o nome do primeiro aluno: '))
alu_2 = str(input('Digite o nome do Segundo Aluno:  '))
alu_3 = str(input('Diite o nome do Terceiro aluno: '))
alu_4 = str(input('Digite o nome do Quarto aluno: '))
sorte = alu_1,alu_2,alu_3,alu_4
sorte = choice(sorte)
print(f'O Aluno escolhido foi {sorte}')