desc = "Controle de estoque de uma pequena loja de informatica"

def Escolha(Texto,NumValidos):
    while True:
        try:
            escolha = int(input(Texto))
            if escolha not in NumValidos:
                print(f"Escolha um numero entre {NumValidos}")
            else:
                return escolha
        except ValueError:
            print("Digite um numero")



produtos = {"Teclado":12, "Mouse":25,"Monitor":4,"Notebook":3,"Headset":8}

while True:
    print("Controle de estoque Loja Gamer 2026")
    print("Lista de funcionalidades: \n[0] Encerrar programa\n[1] Consultar produto\n[2] Listar produtos com baixo estoque\n[3] Dizer o produto com maior estoque")
    escolhaUsuario = Escolha("Use [0,1,2,3] para escolher a funcionalidade\n>",[0,1,2,3])
    match escolhaUsuario:
        case 0:
            break
        case 1:
            while True:
                print("Escolhe qual produto alterar na lista a baixo:")
                print("[0] Voltar")
                for i,produto in enumerate(produtos.keys()):
                    print(f"[{i+1}] {produto}")
                    
                tamanhoEscolha = list(range(len(produtos.keys())))
                tamanhoEscolha.append(len(tamanhoEscolha))
                itemConsultar = Escolha(f"Digite o numero correspondente ao produto para consultar ou sair.\n>",tamanhoEscolha)
                produtoAcessado = list(produtos.keys())[itemConsultar-1]

                if itemConsultar == 0:
                    break
                print(f"Informações do produto:\nNome: {produtoAcessado}\nQuantidade no estoque: {produtos[produtoAcessado]}")
                input()
        case 2:
            pass
        case 3:
            pass
                