# https://forum.python.pro.br/t/reconhecer-padroes-simples-e-desenha-los/40490 #
# Exercício do fórum no link acima #

n = int(input('Digite um número entre 1 e 100: '))
i = 1
padrao1 = []
print('Padrão 01')
for i in range(n):
    padrao1.append('#')
    print(*padrao1)
    i += 1
