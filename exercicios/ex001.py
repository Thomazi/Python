#Escreva uma função para calcular o fatorial de um número.

def fatorial(n):
    if(n == 0):
        return 1
    else:
        return n * fatorial(n-1)
    
n = int(input("Digite o valor de n: "))

print(fatorial(n))
