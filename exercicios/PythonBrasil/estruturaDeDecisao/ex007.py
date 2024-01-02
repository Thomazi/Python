#Faça um Programa que leia três números e mostre o maior e o menor deles. 

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))

maior = n1
menor = n1

if n2 > maior:
    maior = n2
elif n2 < menor:
    menor = n2

if n3 > maior:
    maior = n3
elif n3 < menor:
    menor = n3

print("Maior: {}\nMenor: {}".format(maior, menor))


#maior_numero = max(n1, n2, n3)
#menor_numero = min(n1, n2, n3)