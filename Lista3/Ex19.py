desc = "Binaria True False"

def Init():
    def BinariaTF(lista,Chave):
        inic = 0
        fin = len(lista)-1
        while inic <= fin:
            meio = (inic+fin)//2
            if lista[meio] == Chave:
                return True
            if lista[meio] > Chave:
                fin = meio - 1
            else:
                inic = meio +1
        return False

    lista = [1,2,3,4,5,6,7,8,9,10]
    numero = int(input("Digite o numero para buscar binariamente: "))
    indice = BinariaTF(lista,numero)
    if indice:
        print("Numero na lista")
    else:
        print("Nuero não esta na lista")