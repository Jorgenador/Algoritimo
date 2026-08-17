desc = "Programa de analise de vendas de uma empresa"

def Init():
    vendas = [1250, 980, 1430, 2100, 1750,890, 1620]
    total = sum(vendas)
    media = total/len(vendas)
    maior = vendas[0]
    menor = vendas[0]
    diasMedia = 0

    for i in vendas:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
        if i > media:
            diasMedia +=1

    print(f"Total vendido: R$ {total}")
    print(f"Media Diaria: R$ {media:.2f}")
    print(f"Maior venda: R$ {maior}, Menor venda: R${menor}")
    print(f"Total de dias a cima da media: {diasMedia}")
    print(f"Porcentual de dias a cima da media {((diasMedia/len(vendas)) * 100):.2f}%")