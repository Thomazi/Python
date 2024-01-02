#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar
#sabendo que a decisão é sempre pelo mais barato. 

p1 = float(input("Digite o preço do primeiro produto: "))
p2 = float(input("Digite o preço do segundo produto: "))
p3 = float(input("Digite o preço do terceiro produto: "))

menorPreco = p1

if p2 < menorPreco:
    menorPreco = p2
elif p3 < menorPreco:
    menorPreco = p3

print("O menor preço é: {}".format(menorPreco))