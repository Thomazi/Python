#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 

#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo: 

ganhaPorHora = float(input("Digite quanto voce recebe por hora: "))
horasTrabalhadas = int(input("Digite quantas horas voce trabalha no mes: "))

salarioBruto = ganhaPorHora * horasTrabalhadas
pagoInss = salarioBruto * 0.08
pagoSindicato = salarioBruto * 0.05
pagoImpRenda = salarioBruto * 0.11
salarioLiquido = salarioBruto - (pagoInss + pagoSindicato + pagoImpRenda)

print("Salário bruto: {:.2f}\nPago ao INSS {:.2f}\nPago ao sindicato {:.2f}\nSalário liquido {:.2f}".format(salarioBruto, pagoInss, pagoSindicato, salarioLiquido))


