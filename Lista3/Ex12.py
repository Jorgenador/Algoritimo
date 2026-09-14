desc = "Quase a mesma coisa do cpf, so q tudo"

def Init():
    def BuscaCompleta(Lista,Chave):
        rep, indice = 1,0
        for i in Lista:
            if i == Chave:
                return rep,indice
            rep+=1
            indice+=1
        return rep,-1

    lista = [10,20,30,40,50,60,10,20,30,85]
    numero = int(input("Digite o numro para ser encontrado: "))
    rep,indice = BuscaCompleta(lista,numero)
    if indice != -1:
        print(f"Valor encontrado, numero de comparacoes {rep}, indice {indice}")
    else:
        print(f"{rep} comparacoes feitas e o numero não foi encontrado")


