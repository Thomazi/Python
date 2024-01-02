''' 
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; 

'''

import math
import sys

a = int(input("Digite o valor de A: "))
if a == 0:
    print("A equação não é do segundo grau.")
    sys.exit()

b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = math.pow(b, 2) -4 * a * c
if delta < 0:
    print("A equação não possui raizes reais.")
    sys.exit()
elif delta == 0:
    x = -b/ (2*a)
    print("A equação possui apenas uma raiz real.\nX: {}".format(x))
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("A equação possui duas raizes reais:\nX1: {}\nX2: {}".format(x1, x2))