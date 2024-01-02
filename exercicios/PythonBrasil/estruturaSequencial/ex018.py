#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps)
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 

megaByte = int(input("Digite o tamanho do arquivo(em MB): "))
velLink = int(input("Digite a velocidade do link(em Mbps): "))

velLink = velLink/8
tempo = megaByte/ velLink
tempoEmMinutos = tempo/60

print("O tempo aproximado de dowload(em minutos), sera de: {}".format(tempoEmMinutos))