desc = "Encontrar o segundo maior valor de uma lista sem sort"
def Init():
    # float("-inf") me devolve o menor valor possivel. Descobri isso com resposta automatica de IA (não me orgulho)
    # Mas facilita muito o codigo, já que evita fazer checagens por já me dar um numero muito pequeno
    # Tinha feito um bubble sort manual também, mas acho que assim é melhor
    lista = [10,5,30,20]
    maior = segundo = float("-inf")

    for num in lista:
        if num > maior:
            segundo = maior
            maior = num
        elif num > segundo:
            segundo = num
            
    print(lista)
    print(segundo)