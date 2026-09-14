from buscas import BuscaBinaria
desc = "Lista ordenada e bla bla"

def Init():
    lista = [1,2,3,4,5,6,7,8,9,10]
    numero = int(input("Digite o numero para buscar binariamente: "))
    indice = BuscaBinaria(lista,numero)
    if indice != -1:
        print(f"Numero encontrado no indice {indice}")
    else:
        print("Numero não encontrado")