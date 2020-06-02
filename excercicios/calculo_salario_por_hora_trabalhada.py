'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''

print('Cálculo de salário por horas trabalhadas')
valor_hora = float(input('Digite o valor pago por hora trabalhada em R$:'))
qtd_horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas no mês:'))
salario = valor_hora * qtd_horas_trabalhadas
print(f'O seu salário nesse mês é de R$ {salario:.2f}')
