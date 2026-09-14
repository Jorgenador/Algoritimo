desc = "Busca binaria com exibicao das varaiveis"

def Init():
    def BuscaExibicionist(lista,chave):
        pos_inicial = 0
        pos_final = len(lista)-1

        while pos_inicial <= pos_final:
            pos_meio = (pos_final+pos_inicial) // 2
            print(f"Pos Meio: {pos_meio},Pos Final: {pos_final},Pos Inicial: {pos_inicial}")
            if lista[pos_meio] == chave:
                return pos_meio
            if lista[pos_meio] > chave:
                pos_final = pos_meio-1
            else:
                pos_inicial = pos_meio+1
        return -1

    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    numero = int(input("Digite um numero para ser buscado binariamente: "))
    indice = BuscaExibicionist(lista,numero)
    if indice != -1:
        print(f"Numero econtrado no indice: {indice}")
    else:
        print("Numero não encontrado")