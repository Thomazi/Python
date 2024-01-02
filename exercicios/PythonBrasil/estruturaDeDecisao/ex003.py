#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 

sexo = input("Digite F para feminimo e M para masculino: ").upper()
if sexo == "M":
    print("Masculino.")
elif sexo == "F":
    print("Feminino.")
else:
    print("Sexo inválido.")