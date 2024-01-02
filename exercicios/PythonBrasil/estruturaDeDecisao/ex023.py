"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento. 
"""
n = float(input("Digite um número: "))

if n == round(n):
    print("O número é inteiro.")
else:
    print("O número é decimal.")