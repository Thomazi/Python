#Faça um Programa que peça dois números e imprima o maior deles. 

n1 = int(input("Digite um valor pro primeiro numero: "))
n2 = int(input("Digite um valor pro segundo numero: "))

if n1 > n2:
    print("{}".format(n1))
else:
    print("{}".format(n2))