desc = "Lista de produtos e preços com busca sequencial"

def Init():
    def BuscaDupla(Lista1,Lista2,Chave):
        indice = 0
        for i in Lista1:
            if i == Chave:
                return Lista2[indice]
        return -1

    produtos = ["banana","maca","pera"]
    precos = [3,2,5]

    produto = input("Digite o produto para pesquisar o preço: ").lower()
    preco = BuscaDupla(produtos,precos,produto)
    if preco != -1:
        print(f"Produto {produto} encontrado, preco: R${preco}")
    else:
        print("Produto não encontrado")