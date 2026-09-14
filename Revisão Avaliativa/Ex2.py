motoristas = {}
template = {"Multas Leves":0,"Multas Graves":0,"Multas Gravissimas":0}

def ChecarPericulosidade(nome):
    multas = motoristas[nome]
    multasleves,multasgraves,multasgravissimas = multas["Multas Leves"],multas["Multas Graves"],multas["Multas Gravissimas"]
    if multasgravissimas != 0 or multasgraves > 2:
        return "Motorista Perigoso"
    if sum([multasleves,multasgraves]) == 0:
        return "Motorista Excelente"
    elif multasleves <=2 and multasgraves == 0:
        return "Motorista Bom"
    elif multasleves <=4 and multasgraves <= 1:
        return "Motorista Regular"
    elif multasleves > 4 or multasgraves <= 2:
        return "Motorista Ruim"

while True:
    escolha = int(input("Olá! O que você gostaria de fazer?\n[0] Sair\n[1] Adicionar Multas\n[2] Consultar Situação\n> "))
    match escolha:
        case 0:
            break
        case 1:
            nome = input("Digite o nome do motorista: ")
            motoristas[nome] = template.copy
            for multa in motoristas[nome]:
                motoristas[nome][multa] = int(input(f"Digite a quantidade de {multa}: "))
            situacao = ChecarPericulosidade(nome)
            print(f"Situação final: {situacao}")
        case 2:
            for nome in motoristas:
                situacao = ChecarPericulosidade(nome)
                print(f"{"***"*3}\nMorista: {nome}\nSituação Atual: {situacao}\n{"***"*3}")
        case _:
            print("Opção invalida, tente novamente")