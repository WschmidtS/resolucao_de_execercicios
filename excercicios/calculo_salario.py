"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS.
quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:
Salário Bruto : R$
IR (11%) : R$
INSS (8%) : R$
Sindicato ( 5%) : R$ = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
print('Cálculo de salário')
valor_hora = float(input('Digite o valor pago por hora trabalhada em R$:'))
qtd_horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas no mês:'))
salario_bruto = valor_hora * qtd_horas_trabalhadas
ir = salario_bruto * 0.08
inss = salario_bruto * 0.11
sinticato = salario_bruto * 0.05
descontos = ir + inss + sinticato
salario_liquido = salario_bruto - descontos
print(f'O seu salário bruto nesse mês é de R$ {salario_bruto:.2f}')
print(f'O valor do Imposto de Renda é R$ {ir:.2f}')
print(f'O valor do INSS é R$ {inss:.2f}')
print(f'O valor do Sindicato é R$ {salario_bruto:.2f}')
print(f'O valor total dos descontos é R$ {descontos:.2f}')
print(f'O seu salário líquido nesse mês é de R$ {salario_liquido:.2f}')
