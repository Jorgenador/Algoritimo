desc = "Encontrar maior palavra com busca sequencial"

def Init():
    def BuscaPalavra(Lista):
        maiorPalavra = Lista[0]
        for i in Lista:
            if i > maiorPalavra:
                maiorPalavra = i
        return maiorPalavra

    lista = ["Cabeça","Ombro","pneumoultramicroscopicossilicovulcanoconiótico","Anjos"]
    maiorPalavra = BuscaPalavra(lista)
    print(maiorPalavra)