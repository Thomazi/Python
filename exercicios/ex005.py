#crie um programa que ordene uma lista de números em ordem crescente ou decrescente.

lista = [5,8,2,3,8,42,11,36,4]

lista_crescente = sorted(lista)
lista_decrescente = sorted(lista, reverse=True)

print("Lista crescente: {}\nLista decrescente: {}".format(lista_crescente, lista_decrescente))