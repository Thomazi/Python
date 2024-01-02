#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês. 

salarioPorHora = float(input("Digite quanto voce recebe por hora: "))
horasTrabalhadas = int(input("Digite o numero de horas trabalhadas no mes: "))

totalSalario = salarioPorHora * horasTrabalhadas

print("O salario total referido no mes é de {}".format(totalSalario))