'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
IMC e mostre seu status, de acordo com a tabela absixo:
*Abaixo de 18.5:Abaixo de Peso , *entre 18.5 e 25:Peso ideal
*25 até 30:Sobrepeso , *30 até 40: Obesidade , *Acima de 40: Obesidade Morbida.'''

peso = float(input('Digite seu Peso? (Kg) '))
alt = float(input('Digite sua altura? (m) '))
imc = peso / (alt**2)
print(f'O seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso Ideal')
elif imc >= 25 and imc <= 30:
    print('Está com Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Está em Obesidade')
elif imc >= 40:
    print('Está em Obesidade Morbida')
