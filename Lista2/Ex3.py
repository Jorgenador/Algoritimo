desc = "Criar uma lista com 8 numeros inteiros e exibir a soma dela sem usam sum()"

def Init():
    lista = [10,20,30,40,50,60,70,80]
    soma = 0
    for i in lista:
        soma+=i
    print(soma)