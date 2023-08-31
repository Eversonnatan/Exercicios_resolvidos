'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
*MÉDIA ABAIXO DE 5.0:REPROVADO, * Média entre 5.0 e 6.9:RECUPERAÇÃO
*Média 7.0 ou Superior: APROVADO'''

nota1 = float(input('Digite a Primeira nota: '))
nota2 = float(input('Digite a Segunda nota:  '))
media = (nota1+nota2)/2
print(f'A soma da nota {nota1} e da nota {nota2} \na media do aluno é {media:.1f}')
if media >= 7:
    print('Aluno Aprovado')
elif media >= 5 and media <= 7:
    print('Aluno de Recuperação')
else:
    print('Aluno Reprovado')