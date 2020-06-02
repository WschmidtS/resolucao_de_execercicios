"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro
com metade do segundo . a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo
"""
print('Digite dois números inteiros e um real')
num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
num3 = float(input('Digite o segundo número:'))
result1 = (num1**2) * (num2/2)
print(f'O produto do dobro do primeiro com metade do segundo é: {result1}')
result2 = (3 * num1) + num3
print(f'A soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo: {result2}')
result3 = num3 ** 3
print(f'O terceiro elevado ao cubo é: {result3}')
