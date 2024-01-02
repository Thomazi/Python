#Escreva um programa que gere os primeiros N números da sequência de Fibonacci.

def Fibonacci(n):
    numero1 = 1
    numero2 = 1

    for i in range (n): 
        resultado = numero1 + numero2 
        numero1 = numero2
        numero2 = resultado

    return numero1


n = int(input("Digite n: "))

for i in range (n):
    print(Fibonacci(i))