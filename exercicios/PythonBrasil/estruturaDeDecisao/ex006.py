#Faça um Programa que leia três números e mostre o maior deles. 

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite outro numero: "))

maior = n1

if n2 > maior:
    maior = n2
elif n3 > maior:
    maior = n3

print("maior: {}".format(maior))

# maior_numero = max(n1, n2, n3)