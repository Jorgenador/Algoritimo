# Lista 1 Ex 5: Leia um número inteiro e mostre sua tabuada de 1 a 10.
desc = "Leia um número inteiro e mostre sua tabuada de 1 a 10."
def tabuada(num):
    for i in range(1,11):
        print(num*i)

def Init():
    tabuada(int(input("Escolha um numero para ver a tabuada de 1 ao 10: "))) 
