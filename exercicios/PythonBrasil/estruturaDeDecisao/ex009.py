#Faça um Programa que leia três números e mostre-os em ordem decrescente

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

maior = n1
medio = n2
menor = n3

if n2 > maior:
    maior = n2
    medio = n1
if n3 > maior:
    menor = medio
    medio = maior
    maior = n3
elif n3 > medio:
    menor = medio
    medio = n3
else:
    menor = n3



print("Maior: {}\nMedio: {}\nMenor: {}".format(maior, medio, menor))
