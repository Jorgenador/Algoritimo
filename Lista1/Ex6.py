# Lista 1 Ex 6+: Leia um número N e calcule a soma dos números de 1 até N.
desc = "Leia um número N e calcule a soma dos números de 1 até N."
def ValoresAte(n):
    soma = 0
    for i in range(1,int(n)+1):
        soma+=i
    print(soma)

def Init():
    n = input("Digite um numero inteiro positivo: ")
    ValoresAte(n)
