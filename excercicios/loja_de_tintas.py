"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o
preço total.
"""
import math

print('Programa para cálculo do valor e quantidade de tinta')
metros_quadrado = float(input('Digita a área a ser pintada em m²: '))
lata_metros_quadrado = 18 * 3
if metros_quadrado <= lata_metros_quadrado:
    print(f'Você precisa de apenas 1 lata de tinta\n'
          f'O valor é de R$ 80,00')
elif metros_quadrado > lata_metros_quadrado:
    quantidade_latas = math.ceil(metros_quadrado / lata_metros_quadrado)
    valor = quantidade_latas * 80
    print(f'Você precisa de {quantidade_latas} latas\n'
          f'O valor total é de R$: {valor:.2f}')
