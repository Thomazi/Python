#Faça um Programa que peça as 4 notas bimestrais e mostre a média. 

b1 = float(input("Digite a nota do b1: "))
b2 = float(input("Digite a nota do b2: "))
b3 = float(input("Digite a nota do b3: "))
b4 = float(input("Digite a nota do b4: "))

media = (b1+b2+b3+b4) / 4

print("A média das notas bimestrais é: {}".format(media))