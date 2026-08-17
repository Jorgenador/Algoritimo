desc = "Informar quantas vezes um numero se repete me uma lista"

# Não usando .Count
def Init():
    numeros =  [2, 3, 2, 5, 3, 2,5,10,10,10]
    listados = []
    for i in numeros:
        if i in listados:
            continue
        repeticao = 0
        numero = None
        numero = i
        for repetido in numeros:
            if numero == repetido:
                repeticao+=1
        listados.append(numero)
        print(f"O numero: {numero}, se aparece {repeticao} vezes na lista.")


    #usando count:
    #   for i in numeros:
    #      if i not in listados:
    #           repeticoes = numeros.count(i)
    #           print(f"O numero {i} aparece {repeticoes} na lista")
    #           listados.append(i)