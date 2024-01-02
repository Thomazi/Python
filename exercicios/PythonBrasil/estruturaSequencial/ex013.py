#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7 

sexo = input("Digite H se for homem e M se for mulher: ").upper()
if sexo == "H":
    altura = float(input("Digite a altura: "))
    pesoIdealHomem = (72.7*altura) - 58
    print("Peso ideal homem: {:.2f}".format(pesoIdealHomem))
elif sexo == "M":
    altura = float(input("Digite a altura: "))
    pesoIdealMulher = (62.1*altura) - 44.7
    print("Peso ideal mulher: {:.2f}".format(pesoIdealMulher))
else:
    print("Sexo inválido.")
