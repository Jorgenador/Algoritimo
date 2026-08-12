desc = "Busque um elemento na lista sem usar index()"

def Init():
    lista = list(map(int,input("Digite 8 numeros e os separe com espaço: ").split(" ")))
    numeroPesquisar = int(input("Digite um numero para encontar na lista: "))

    for i,numero in enumerate(lista):
        if numero == numeroPesquisar:
            print(f"Numero {numeroPesquisar} na lista no indice {i+1}")