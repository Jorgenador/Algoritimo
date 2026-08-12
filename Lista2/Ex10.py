desc = "Exibir a lista, depois a lista sort e sorted"
def Init():
    numeros = [18, 5, 12, 3, 20, 7, 9]
    print(numeros)
    numeroSorted = sorted(numeros) # Devolve a lista ou outra entrada organizada
    print(numeroSorted)
    numeros.sort() # Atualiza a lista diretamente sem devolver uma nova
    print(numeros)