# Lista 1 Ex 10: Desafio: Faça um programa que leia 5 números e informe o maior e o menor valor.
desc = "Desafio: Faça um programa que leia 5 números e informe o maior e o menor valor."
def Ordenador(n):
    n.sort()
    print(f"O menor numero é: {n[0]}, o maior numero é {n[len(n)-1]}")

def Init():
    Ordenador(list(map(int,input("Digite uma lista de numeros, te devolverei o maior e o menor(separe-os com espaço): ").split())))