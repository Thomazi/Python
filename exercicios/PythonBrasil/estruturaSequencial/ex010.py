#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. 
##C = 5 * ((F-32) / 9).

tempCelsius = float(input("Digite a temperatura em Celsius: "))
tempFahrenheit = ((9 * tempCelsius) / 5) + 32

print("Temperatura em Fahrenheit: {:.2f}".format(tempFahrenheit))