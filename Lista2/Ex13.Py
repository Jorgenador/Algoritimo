desc = "Ler 10 numeros, os armazenar em uma lista, calclar a media e exibir os numeors a cima media"

def Init():
    lista = list(map(float,input("Digite 10 numeros e os separe com espaço: ").split(" ")))
    listaAcima = [i for i in lista if i > (sum(lista)/len(lista))]
    print(f"Media: {sum(lista)/len(lista):.2f}")
    print(listaAcima)