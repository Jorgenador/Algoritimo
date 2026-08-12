# Lista 1 Ex 1: Soma, subtração, divisão e multiplicação dos numeros (Fiz com function pra facilitar)

desc = "Soma, subtração, divisão e multiplicação dos numeros"

def OpBasicas(n1,n2):
    print(f"Soma dos numeros: {n1+n2}")
    print(f"Subtração dos numeros: {n1-n2}")
    print(f"Divisão dos numeros: {n1/n2}")
    print(f"Multiplicação dos numeros: {n1*n2}")

def Init():
    n1 = int(input("Digite o primeiro numero!: "))
    n2 = int(input("Digite o segundo numero!: "))
    OpBasicas(n1,n2)


