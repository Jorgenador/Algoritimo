# Lista 1 Ex 6+: Receba 2 numeros, compare-os e devolva o maior/menor.
desc = "Receba 2 numeros, compare-os e devolva o maior/menor."
def MaiorNum(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2


def Init():
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    print(MaiorNum(n1,n2))