# Lista 1 Ex 7: Leia 10 números e informe a soma e a média.
desc = "Leia 10 números e informe a soma e a média."
def SomaMedia(n):
    print(f"A soma dos valores é: {sum(n)}")
    print(f"A media dos valores é: {sum(n)/len(n)}")

def Init():
    SomaMedia(list(map(int,(input("Me de uma lista separada com espaço dos valores para serem somados: ").split()))))
