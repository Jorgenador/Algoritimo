desc = "Criar uma lista, exibir os valores da lista em linhas diferentes após isso exiba os valores maiores que 10"
def Init():
    numeros = [7, 12, 5, 18, 3, 20]
    numMaiorDez = []
    for i in numeros:
        print(i)
        if i > 10:
            numMaiorDez.append(i)
    print(numMaiorDez)