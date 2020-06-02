"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7
"""
print('Programa para calcular o peso ideal')
genero = int(input('Digite 1 para Homem ou 2 para Mulher: '))
h = float(input('Digite a sua altura em metros: '))

if genero == 1:
    peso_ideal = (72.7 * h) - 58
    print(f'O seu peso ideal é {peso_ideal:.2f} Kg')
elif genero == 2:
    peso_ideal = (62.1 * h) - 44.7
    print(f'O seu peso ideal é {peso_ideal:.2f} Kg')


