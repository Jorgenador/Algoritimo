import random
desc = "Lista de numeros aleatorios, dizer toda as posições deles"

def Init():
    def BuscaRandom(lista,chave):
        indices = []
        indice = 0
        for i in lista:
            if i == chave:
                indices.append(indice)
            indice+=1
        if len(indices) != 0:
            return indices
        else:
            return -1

    lista = []

    for i in range(20):
        lista.append(random.randint(1,10))

    numero = int(input("Digite um numero para ver quantas vezes aparece na lista(A lista possui valores entre 1 e 10): "))
    indices = BuscaRandom(lista,numero)
    if indices != -1:
        print(f"O numero aparece nas posicoes {indices}")
    else:
        print("O numero não aparece na lista")

