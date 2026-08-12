desc = "Contar a quantidade de pares e impares em uma lista"

def Init():
    lista = [1,2,3,4,5,6,7,8,9,10]
    print(lista)
    par = []
    impar = []
    for i in lista:
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i)
    print(f"Valores impares: {impar}, valores pares: {par}")