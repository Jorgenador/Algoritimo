desc = "Calcular a média de uma lista e informar a média de forma manual (sem len/sum)"

def Init():
    notas = [7.5, 8.0, 6.0, 9.5, 5.5]
    soma = 0
    quantidade = 0
    for i in notas:
        soma += i
        quantidade+=1
    media = soma/quantidade
    print(f"{media:.2f}")