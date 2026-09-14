desc = "Busca sequencial personalizada"

def Init():
    def BuscaPerso(Lista,Chave):
        rep = 0
        for i in Lista:
            if i == Chave:
                rep += 1
        if rep == 0:
            return -1
        else:
            return rep
                

    notas = [5,10,4,3,2,5.2,5.5,6,7.1,5]

    nota = float(input("Digite a nota para ser pesquisada: "))
    indice = BuscaPerso(notas,nota)

    if indice != -1:
        print(f"Nota está na lista e aparece {indice} vezes")
    else:
        print("Nota não está na lista")