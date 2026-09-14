desc = "Busca True, False"

def Init():
    def BuscaTF(Lista,Chave):
        for i in Lista:
            if i == Chave:
                return True
        return False

    lista = [10,5,20,25,30]

    numero = int(input("Digite o numero para ser buscado na lista: "))
    if BuscaTF(lista,numero):
        print("Numero na lista")
    else:
        print("Numero não está na lista")