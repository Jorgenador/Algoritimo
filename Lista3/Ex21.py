desc = "Busca binaria repetida"

def Init():
    def BinariRepetida(lista,chave):
        indices = []
        inic = 0
        fin = len(lista)-1
        while inic <= fin:
            meio = (inic+fin)//2
            if lista[meio] == chave:
                indices.append(meio)
            if lista[meio] > chave:
                fin = meio-1
            else:
                inic = meio +1
        if len(indices) != 0:
            return indices
        else:
            return -1

    lista = [1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10]
    numero = int(input("Digite o numero para buscar binariamente: "))
    indice = BinariRepetida(lista,numero)
    if indice != -1:
        print(f"Numero na lsita nos indices: {indice}")
    else:
        print("Numero não está na lista")