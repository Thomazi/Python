#Crie um programa que verifique se uma palavra é um palíndromo.

def eh_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    inverso = palavra[::-1]

    if palavra == inverso:
        return True
    else:
        return False


palavra = str(input("Digite uma palavra para verificar se é um palíndromo: "))
if(eh_palindromo(palavra)):
    print("A palavra é um palindromo.")
else:
    print("Não é um palindromo")