"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
import math

print('Programa para cálculo do valor e quantidade de tinta')
metros_quadrado = float(input('Digita a área a ser pintada em m²: '))
lata_metros_quadrado = 18 * 6
galao_metros_quadrado = 3.6 * 6
if metros_quadrado <= galao_metros_quadrado:
    print(f'Você precisa de apenas 1 galão de tinta\n'
          f'O valor é de R$ 25,00')
if galao_metros_quadrado < metros_quadrado <= lata_metros_quadrado:
    quantidade_latas = math.ceil(metros_quadrado / galao_metros_quadrado)
    valor = quantidade_latas * 25
    print(f'Você precisa de {quantidade_latas} galões\n'
          f'O valor total é de R$: {valor:.2f}')
if
    '''
    Falta terminar!!! Travou na lógica!
    '''