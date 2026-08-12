desc = "Listas paralelas com nome de 5 alunos e suas notas, percorer as duas simultaneamnete e exibir aprovação se maior que 5"
def Init():
    alunos = ["Bernardo","Pedro","Joao","Gustavo","Ricardo"]
    notas = [6,10,8,5,3]

    #Forma que eu pensei inicialmente:
    #   for i in range(5):
    #        if notas[i] >= 6:
    #            print(f"{alunos[i]} foi aprovado")
    #       else:
    #            print(f"{alunos[i]} foi reprovado")

    # Forma alternativa:
    
    for aluno,nota in zip(alunos,notas):
        if nota >= 6:
            print(f"{aluno} foi aprovado!")
        else:
            print(f"{aluno} foi reprovado")