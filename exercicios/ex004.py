#Faça um programa que conte o número de vogais em uma palavra.

def conta_vogal(palavra):
    vogal = 0
    for i in range (len(palavra)):
        if palavra[i] == "a" or palavra[i] == "e" or palavra[i] == "i" or palavra[i] == "o" or palavra[i] == "u":
            vogal+= 1
    return vogal

palavra = str(input("Digite a palavra: "))
print(conta_vogal(palavra))