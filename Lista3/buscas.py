def BuscaSequencial(Lista,Chave):
    indice = 0
    for i in Lista:
        if i == Chave:
            return indice
        indice+=1
    return -1

def BuscaBinaria(Lista,Chave):
    pos_inic = 0
    pos_final = len(Lista)

    while pos_inic <= pos_final:
        pos_meio = (pos_inic+pos_final) // 2

        if Lista[pos_meio] == Chave:
            return pos_meio
        if Lista[pos_meio] > Chave:
            pos_final = pos_meio - 1 
        else:
            pos_inic = pos_meio + 1

    return -1
