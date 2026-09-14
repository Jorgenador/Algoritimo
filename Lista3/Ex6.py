desc = "Encontrar o maior valor baseado em busca sequencial"

def Init():
    def BuscaMaior(Lista):
        maiorValor = Lista[0]
        for i in Lista:
            if i > maiorValor:
                maiorValor = i
        return maiorValor

    lista = [10,50,40,30,20,125,200]
    maiorValor = BuscaMaior(lista)
    print(maiorValor)