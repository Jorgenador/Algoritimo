from buscas import BuscaBinaria
desc = "Numeros pares com busca binaria"
def Init():
    lista = []
    for i in range(2,201):
        if i % 2 == 0:
            lista.append(i)

    numero = int(input("Digite o numero par para buscar binariamente: "))
    indice = BuscaBinaria(lista,numero)
    if indice != -1:
        print("Numero na lista!!")
    else:
        print("Numero não está na lista")