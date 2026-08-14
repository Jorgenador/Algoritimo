import os
import time
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
            print("Apenas numeros são aceitos")

def AlterarEstoque(lista,Produto):
    while True:
        print(f"Quantidade atual: {lista[Produto]}")
        try:
            nova_quantia = int(input("Digite a nova quantidade: "))
            lista[Produto] = nova_quantia
            os.system("cls")
            break
        except ValueError:
            print("Apenas numeros são aceitos")

produtos = {"Teclado":12, "Mouse":25,"Monitor":4,"Notebook":3,"Headset":8}
def Init():
    while True:
        os.system("cls")
        print("Controle de estoque Loja Gamer 2026")
        print("Lista de funcionalidades: \n[0] Encerrar programa\n[1] Consultar produto\n[2] Listar produtos com baixo estoque\n[3] Dizer o produto com maior estoque")
        escolhaUsuario = Escolha("Use [0,1,2,3] para escolher a funcionalidade\n>",[0,1,2,3])
        match escolhaUsuario:
            case 0:
                break
            case 1:
                while True:
                    os.system("cls")
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
                    os.system("cls")
                    print(f"Informações do produto:\nNome: {produtoAcessado}\nQuantidade no estoque: {produtos[produtoAcessado]}")
                    print("Gostaria de alterar a quantidade?\n[0] Não\n[1] Sim")
                    alterar = Escolha("Use [0,1] para escolher a opção.\n>",[0,1])
                    if alterar == 1:
                        AlterarEstoque(produtos,produtoAcessado)
                        print(f"Quantidade atual: {produtos[produtoAcessado]}")
                        time.sleep(.75)
            case 2:
                print("Lista de produtos com menos de 5 unidades")
                for i in produtos:
                    if produtos[i] <= 5:
                        print(f"{i} está com baixo estoque, estoque atual: {produtos[i]}")
                input("Pressione enter para continuar")
            case 3:
                maiorItem= None
                maiorQuantia = None
                for item,numero in produtos.items():
                    if maiorItem == None:
                        maiorItem = item
                        maiorQuantia = numero
                    elif numero > maiorQuantia:
                        maiorItem = item
                        maiorQuantia = numero
                print(f"O item com maior quantia em estoque é {maiorItem} com {maiorQuantia} em estoque.")
                input("Digite enter para continuar")
                