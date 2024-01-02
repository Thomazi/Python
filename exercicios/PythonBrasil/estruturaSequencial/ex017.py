#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: 
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima
#isto é, considere latas cheias. 
import math

tamanhoMetrosQuadrados = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
quantidadeDeLitros = tamanhoMetrosQuadrados/6
quantidadeDeLitrosComFolga = quantidadeDeLitros * 1.1

quantidadeDeLatas = math.ceil(quantidadeDeLitrosComFolga / 18)
precoLata = quantidadeDeLatas * 80.00

quantidadeDeGaloes = math.ceil(quantidadeDeLitrosComFolga / 18)
precoGalao = quantidadeDeGaloes * 25.00

quantidaDeLatasMix = quantidadeDeLitrosComFolga // 18
restoLitros = quantidadeDeLitrosComFolga % 18
quantidadeDeGaloesMix = math.ceil(restoLitros/3.6)
precoMix = (quantidaDeLatasMix * 80.00) + (quantidadeDeGaloesMix * 25.00)

print("Se comprar apenas latas, com o tamanho de metros quadrados de {}, o preço fica a: {}".format(tamanhoMetrosQuadrados, precoLata))
print("Se comprar apenas galoes, com o tamanho do metro quadrado de {}, o preco fica a: {}".format(tamanhoMetrosQuadrados, precoGalao))
print("Se comprar latas e galoes, com metro quadrado de {}, o preço sairia a: {}".format(tamanhoMetrosQuadrados, precoMix))

