# Lista 1 Ex 3: Leia um número e informe se ele é positivo, negativo ou zero.
desc = "Leia um número e informe se ele é positivo, negativo ou zero."
def ChecarNum(n):
    if n > 0:
        print("Numero positivo!")
    elif n < 0:
        print("Numero negativo!")
    else:
        print("O numero é 0")

def Init():
    ChecarNum(int(input("Digite um numero para a checagem: ")))

