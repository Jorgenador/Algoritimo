from buscas import BuscaSequencial
desc = "Peça uma matricula e pesquisa sobre ela"

def Init():
    matriculas = [110,111,112,113,114,115]
    matriculaAluno = int(input("Digite a matricula do aluno para buscar: "))

    if BuscaSequencial(matriculas,matriculaAluno) != -1:
        print("Aluno matriculado")
    else:
        print("O aluno não está matriculado")