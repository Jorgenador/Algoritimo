import buscas
desc = "Busca sequencial para encontrar numero inteiro"

def Init():
    lista = [1,2,3,4,5,6,7,8,9,10]

    numero = int(input("Digite o numero para ser buscado dentro da lista:"))
    indice = buscas.BuscaSequencial(lista,numero)
    if indice != -1:
        print(f"Numero encontrado, indice {indice}")