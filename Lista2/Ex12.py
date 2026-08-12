desc = "Criar uma nova lista com base na lista dada sem repetir valores"

def Init():
    numeros = [2, 5, 2, 8, 5, 9, 2, 8, 10]
    numerosSemRepetir = list(dict.fromkeys(numeros))

    print(numeros)
    print(numerosSemRepetir)
