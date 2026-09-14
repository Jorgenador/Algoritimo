desc = "Busca binaria contada"

def Init():
    def BinariaContada(lista,chave):
        posInic = 0
        posFin = len(lista)-1
        reps = 1
        while posInic <= posFin:
            posMeio = (posFin + posInic) // 2

            if lista[posMeio] == chave:
                return posMeio,reps
            if lista[posMeio] > chave:
                posFin = posMeio-1
            else:
                posInic = posMeio+1
            reps += 1
        return -1,reps

    lista = [1,2,3,4,5,6,7,8,9,10]
    numero = int(input("Digite o numero para buscar binariamente: "))
    indice,reps = BinariaContada(lista,numero)
    if indice != -1:
        print(f"Numero encontrado no indice {indice} encontrado depois de {reps} comparacoes")
    else:
        print(f"Numero não encontrado, {reps} comparacoes feitas.")