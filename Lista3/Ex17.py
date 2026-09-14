from buscas import BuscaBinaria
desc = "Codigo de produtos so q com busca binaria agr"
def Init():
    codigos = [10,11,12,13,14,15]
    numero = int(input("Digite o codigo do produto: "))
    indice = BuscaBinaria(codigos,numero)
    if indice != -1:
        print("O produto está cadastrado")
    else:
        print("O produto não está cadastrado")


