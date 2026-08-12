# Lista 1 Ex 8: Leia varios numeros até o usuario digitar 0 depois de a soma dos valores 
desc = "Leia varios numeros até o usuario digitar 0 depois de a soma dos valores"

def Numeros():
    numero = int(input("Digite o primeiro numero para começar (digite 0 para finalizar): "))
    soma = 0
    qntNum = 0
    while numero != 0:
        qntNum += 1
        soma += numero
        numero = int(input("Digite o próximo numero!: "))
    print(f"A soma de todos os numeros foi: {soma}, {qntNum} numeros digitados.")

def Init():
    Numeros()

