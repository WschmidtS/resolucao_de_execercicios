"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
print('Cálculo do tempo de Download de um Arquivo')
arquivo = float(input('Digite o tamanho do arquivo para Download em Mb: '))
link_internet = int(input('Digite a velocidade do Link de Internet em Mbps: '))
tempo_download = arquivo / (link_internet / 8)
if tempo_download < 60:
    tempo_download = round(tempo_download)
    print(f'Tempo de Download são aproximadamente: {tempo_download} segundos')
elif tempo_download >= 60:
    tempo_download = round(tempo_download / 60)
    print(f'Tempo de Download são: {tempo_download} minutos')
