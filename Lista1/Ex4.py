# Lista 1 Ex 4: Ler a nota do aluno e > 7 aprovado, caso contrario reprovado
desc = "Ler a nota do aluno e > 7 aprovado, caso contrario reprovado"
def ChecarAprov(nota):
    if nota > 7:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")

def Init():
    ChecarAprov(int(input("Digite sua nota: ")))

