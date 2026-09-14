from buscas import BuscaBinaria
desc = "Lista ordenada de nomes, implementar busca bianria blabla"

def Init():
    nomes = ['andre', 'carlos', 'emanoel', 'felipe', 'joao']
    nome = input("Digite um nome para pesquisar: ").lower()
    indice = BuscaBinaria(nomes,nome)
    if indice != -1:
        print(f"Nome encontrado no indice: {indice}")
    else:
        print("Nome não encontrado")