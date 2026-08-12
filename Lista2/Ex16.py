desc = "Lista de listas, criar uma matriz 3x3 e a soma das linhas"
def Init():
    matriz = [[1,1,1],[2,2,2],[3,3,3]]
    print(matriz)
    soma = 0
    for i,lista in enumerate(matriz):
        print(f"Linha {i+1} vale:{sum(lista)}")
        soma += sum(lista)
    print(f"Total de todas linhas: {soma}")