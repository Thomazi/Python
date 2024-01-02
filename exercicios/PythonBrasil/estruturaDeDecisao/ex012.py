#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto
#mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. 

#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
#No exemplo o valor da hora é 5 e a quantidade de hora é 220. 

valorHora = float(input("Digite quanto voce recebe por hora: "))
quantidadeDeHorasTrabalhadas = int(input("Digite quantas horas voce trabalha no mês: "))

salarioBruto = valorHora * quantidadeDeHorasTrabalhadas
percImpRenda = float
descontoImpRenda = float

if salarioBruto <= 900:
    percImpRenda = 0
    descontoImpRenda = salarioBruto * 0
elif salarioBruto > 900 and salarioBruto <= 1500:
    percImpRenda = 5
    descontoImpRenda = salarioBruto * 0.05
elif salarioBruto > 1500 and salarioBruto <= 2500: 
    percImpRenda = 10
    descontoImpRenda = salarioBruto * 0.10
else:
    percImpRenda = 20
    descontoImpRenda = salarioBruto * 0.20


descontoInss = salarioBruto * 0.10
aumentoFgts = salarioBruto * 0.11
totalDescontos = descontoImpRenda + descontoInss
salarioLiquido = salarioBruto - totalDescontos

print("\n\nSalário Bruto: ({} * {})            :R$ {}".format(valorHora, quantidadeDeHorasTrabalhadas, salarioBruto))
print("(-) IR ({}%)                           :R$ {}".format(percImpRenda, descontoImpRenda))
print("(-) INSS (10%)                        :R% {}".format(descontoInss))
print("FGTS (11%) depositado pela empresa    :R$ {}".format(aumentoFgts))
print("Total de descontos                    :R$ {}".format(totalDescontos))
print("Salário Liquido                       :R$ {}".format(salarioLiquido))