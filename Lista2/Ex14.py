desc = "Criara lista com compreensão de lista com quadrados, pares, numeros maiores que 5"

def Init():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numerosQuadrados = [i**2 for i in numeros]
    numerosPares = [i for i in numeros if i % 2 == 0]
    numerosMaioresQueCinco = [i for i in numeros if i > 5]

    print(f"Lista original: {numeros}")
    print(f"Lista com os numeros ao quadrado: {numerosQuadrados}")
    print(f"Lista somente com os pares: {numerosPares}")
    print(f"Lista somente com os maiores que cinco: {numerosMaioresQueCinco}")