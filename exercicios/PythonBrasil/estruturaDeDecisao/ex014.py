#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
#e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: 

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2
conceito = str
mensagem = str

if media >= 9.0 and media <=10:
    conceito = "A"
    mensagem = "APROVADO"
elif media >= 7.5 and media < 9.0:
    conceito = "B"
    mensagem = "APROVADO"
elif media >= 6.0 and media < 7.5:
    conceito = "C"
    mensagem = "APROVADO"
elif media >= 4.0 and media < 6.0:
    conceito = "D"
    mensagem = "REPROVADO"
else: 
    conceito = "E"
    mensagem = "REPROVADO"

print("Nota 1ºBim: {}\nNota 2ºBim: {}".format(n1, n2))  
print("Média do aluno: {}\nConceito: {}".format(media, conceito))
print("O aluno foi {}".format(mensagem))
