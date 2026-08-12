desc = "Criar uma lista qualquer e determinar o maior e o menor valor manualmente"

def Init():
    lista = [10,5,15,20,25,30]
    maior = lista[0]
    menor = lista[0]
    for i in lista:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
    print(menor,maior)

