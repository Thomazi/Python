#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual: 

#salários até R$ 280,00 (incluindo) : aumento de 20% 
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento. 

salarioColaborador = float(input("Digite o salario do colaborador: "))
novoSalario = float
percentual = float

if salarioColaborador <= 280.00:
    novoSalario = salarioColaborador * 1.20
    percentual = 20
elif salarioColaborador > 280.00 and salarioColaborador <= 700.00:
    novoSalario = salarioColaborador* 1.15
    percentual = 15
elif salarioColaborador > 700.00 and salarioColaborador <= 1500.00:
    novoSalario = salarioColaborador * 1.10
    percentual = 10
else:
    novoSalario = salarioColaborador * 1.05
    percentual = 5

valorDoAumento = novoSalario - salarioColaborador



print("Salário antes do reajuste: R$ {}\nPercentual de aumento aplicado: {}%\nValor do aumento: R$ {}\nNovo salário: R$ {}".format(salarioColaborador, percentual, valorDoAumento,novoSalario))
