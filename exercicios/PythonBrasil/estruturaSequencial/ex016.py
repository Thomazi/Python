#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros
#que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
import math

metrosQuadrados = int(input("Digite o tamanho em metros quadrados da area a ser pintada: "))
quantidadeDeLitros = metrosQuadrados / 3
quantidadeDeLatas = quantidadeDeLitros/18
quantidadeDeLatas = math.ceil(quantidadeDeLatas)

preco = quantidadeDeLatas * 80

print("Quantidade de latas de tinta a serem compradas {}, preço final: {:.2f}".format(quantidadeDeLatas, preco))
