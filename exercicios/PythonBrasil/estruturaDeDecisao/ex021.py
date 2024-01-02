'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas
de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5
e quatro notas de 1. 
'''
valorSaque = float(input("Digite o valor do saque: "))

if valorSaque < 10 or valorSaque > 600:
    print("Erro: valor de saque")
else:
    notacem = int(valorSaque / 100)
    valorSaque = valorSaque - (100 * notacem)

    notacinquenta = int(valorSaque / 50)
    valorSaque = valorSaque - (50 * notacinquenta)
    
    notadez = int(valorSaque / 10)
    valorSaque = valorSaque - (10 * notadez)

    notacinco = int(valorSaque / 5)
    valorSaque = valorSaque - (5 * notacinco)

    um = valorSaque

    print(f"o programa fornece {notacem} de 100, {notacinquenta} de 50, {notacinco} de 5 e {um:.0f} nota de 1")
