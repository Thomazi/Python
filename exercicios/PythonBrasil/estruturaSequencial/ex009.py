#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9). 

tempFahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
tempCelsius = 5 * ((tempFahrenheit-32)/9)

print("A temperatura de Fahrenheit para Celsius é {:.2f}".format(tempCelsius))