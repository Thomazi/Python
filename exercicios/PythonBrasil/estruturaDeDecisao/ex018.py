#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. 

from datetime import datetime

def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%y")
        return True
    except ValueError:
        return False

data = int(input("Digite uma determinada data(dd/mm/aaaa): "))

if validar_data(data):
    print("A data é verdadeira.")
else:
    print("A data é falsa.")

