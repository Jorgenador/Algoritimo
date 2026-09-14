def CalcularProduto():
    produto = float(input("Insira o valor do produto\n> "))
    print(f"O valor do Produto com imposto é R${produto*1.18}")

def CalcularServico():
    servico = float(input("Insira o valor do produto\n> "))
    print(f"O valor do Produto com imposto é R${servico*1.18}")


while True:
    escolha = int(input("Olá! Gostaria de calcular o imposto? Escolha as opções\n[0] Sair\n[1] Calcular Produto\n[2] Calcular Servico\n> "))
    match escolha:
        case 0:
            break
        case 1:
            CalcularProduto()
        case 2:
            CalcularServico()
        case _:
            print("Opção invalida, tente novamente.")