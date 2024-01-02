#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math 

raio = float(input("Digite o raio do circulo: "))
area = raio * 2 * math.pi 

print("Um circulo com raio {} tem a área igual a: {:.2f}".format(raio, area))