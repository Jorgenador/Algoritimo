desc = "Posições de elementos na tabela"

def Init():
    nomes = ["ana", "bruno", "carlos", "daniel", "eduarda"]
    nome = input(f"Digite nomes entre: {nomes}, te informarei a posição dele na lista: ")

    try:
        posicao = (nomes.index(nome.lower()) +1)
        print(f"O nome está na posição: {posicao}")
    except ValueError:
        print("Nome não está na lista")
