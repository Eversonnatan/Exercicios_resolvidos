#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Emque posição ela aparece a Primeira vez
#Em que posição ela aparece a ultima vez
frase = str(input('Digite uma Frase:  ')).strip().lower().replace(' ','')
print(frase)
print('A Sua Frase possui ',frase.count('a'),'de A')
print('A Letra A aparece na posição ',frase.find('a')+1)
print('a Letra A aparece pela ultima vez na posição',frase.rfind('a')+1)