# Lista 1 Ex 6+: Leia um número N e calcule a soma dos números de 1 até N.
def ValoresAte(n):
    soma = 0
    for i in range(1,int(n)+1):
        soma+=i
    print(soma)

n = input("Digite um numero inteiro positivo: ")
ValoresAte(n)

# Lista 1 Ex 1: Soma, subtração, divisão e multiplicação dos numeros (Fiz com function pra facilitar)

def OpBasicas(n1,n2):
    print(f"Soma dos numeros: {n1+n2}")
    print(f"Subtração dos numeros: {n1-n2}")
    print(f"Divisão dos numeros: {n1/n2}")
    print(f"Multiplicação dos numeros: {n1*n2}")

n1 = int(input("Digite o primeiro numero!: "))
n2 = int(input("Digite o segundo numero!: "))
OpBasicas(n1,n2)

# Lista 1 Ex 2: Leia a idade e nome de uma pessoa e apresente esses dados

nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá {nome}, muito bom saber que você possui {idade} anos!!")

# Lista 1 Ex 3: Leia um número e informe se ele é positivo, negativo ou zero.

def ChecarNum(n):
    if n > 0:
        print("Numero positivo!")
    elif n < 0:
        print("Numero negativo!")
    else:
        print("O numero é 0")

ChecarNum(int(input("Digite um numero para a checagem: ")))

# Lista 1 Ex 4: Ler a nota do aluno e > 7 aprovado, caso contrario reprovado

def ChecarAprov(nota):
    if nota > 7:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")

ChecarAprov(int(input("Digite sua nota: ")))

# Lista 1 Ex 5: Leia um número inteiro e mostre sua tabuada de 1 a 10.
def tabuada(num):
    for i in range(1,11):
        print(num*i)

tabuada(int(input("Escolha um numero para ver a tabuada de 1 ao 10: "))) 

# Lista 1 Ex 7: Leia 10 números e informe a soma e a média.

def SomaMedia(n):
    print(f"A soma dos valores é: {sum(n)}")
    print(f"A media dos valores é: {sum(n)/len(n)}")

SomaMedia(list(map(int,(input("Me de uma lista separada com espaço dos valores para serem somados: ").split()))))

# Lista 1 Ex 8: Leia varios numeros até o usuario digitar 0 depois de a soma dos valores 

def Numeros():
    numero = int(input("Digite o primeiro numero para começar (digite 0 para finalizar): "))
    soma = 0
    qntNum = 0
    while numero != 0:
        qntNum += 1
        soma += numero
        numero = int(input("Digite o próximo numero!: "))
    print(f"A soma de todos os numeros foi: {soma}, {qntNum} numeros digitados.")

Numeros()

# Lista 1 Ex 9: Função de 2 numeros e devolve o maior

def MaiorNum(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
print(MaiorNum(n1,n2))
# Lista 1 Ex 10: Desafio: Faça um programa que leia 5 números e informe o maior e o menor valor.

def Ordenador(n):
    n.sort()
    print(f"O menor numero é: {n[0]}, o maior numero é {n[len(n)-1]}")

Ordenador(list(map(int,input("Digite uma lista de numeros, te devolverei o maior e o menor(separe-os com espaço): ").split())))