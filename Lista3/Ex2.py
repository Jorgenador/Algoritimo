from buscas import BuscaSequencial
desc = "Busca sequencial em lista de nomes"

def Init():
    lista = ["joao","carlos","andre","julio"]

    nome = input("Digite um nome para ser pesquisado na lista: ").lower()
    indice = BuscaSequencial(lista,nome)

    if indice != -1:
        print(f"Nome encontrado no indice {indice}")
    else:
        print("Nome não presente na lista")