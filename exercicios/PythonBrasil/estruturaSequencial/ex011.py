#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#A) o produto do dobro do primeiro com metade do segundo .
#B) a soma do triplo do primeiro com o terceiro.
#C) o terceiro elevado ao cubo.
import math

n1 = int(input("Digite o primeiro numero: ")) 
n2 = int(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))

a = (2 * n1) * (n2/2)
b = (3 * n1) + (n3)
c = math.pow(n3,2)

print("A = {}\nB = {}\nC = {}".format(a, b, c))