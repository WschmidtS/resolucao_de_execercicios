'''
Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
'''

print('Conversor de Temperatura de Farenheit para Celsius')
farenheit = float(input('Digite a temperatura em Farenheit:'))
celsius = (5 * (farenheit - 32) / 9)
print(f'A temperatura em Celsius é {celsius:.2f} Cº')
