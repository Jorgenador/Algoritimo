import os
import time
class Tabuleiro:

    def __EncontarCasas(self):
        linha,coluna = self.LocCavalo[0],self.LocCavalo[1]
        

        if self.CasasMovimentar:
            for i in self.CasasMovimentar:
                self.Tabuleiro[i[0]][i[1]] = "."
            self.CasasMovimentar = []

        if self.LocAntiga:
            linhaA,colunaA = self.LocAntiga
            self.Tabuleiro[linhaA][colunaA] = "."

        for i in [2,-2]:
            dir = linha-i
            if dir >= 0 and dir <= 7:
                for j in [1,-1]:
                    dir2 = coluna-j
                    if dir2 >= 0 and dir2 <= 7:
                        self.CasasMovimentar.append((dir,dir2))

        for i in [2,-2]:
            dir = coluna-i
            if dir >= 0 and dir <= 7:
                for j in [1,-1]:
                    dir2= linha-j
                    if dir2 >= 0 and dir2 <= 7:
                        self.CasasMovimentar.append((dir2,dir))

        for i in self.CasasMovimentar:
            self.Tabuleiro[i[0]][i[1]] = "*"

        self.Tabuleiro[linha][coluna] = "X"
        self.LocAntiga = self.LocCavalo


    def __GeraTabuleiro(self):
        return [["." for i in range(8)] for j in range(8)]

    def __init__(self):
        self.Tabuleiro = self.__GeraTabuleiro()
        self.CasasMovimentar =[]
        self.LocAntiga = None
        self.LocCavalo = None

    def PrintarTabuleiro(self):
        print("  ",end="")
        for num in range(len(self.Tabuleiro)):
            print(f" {num} ",end="")
        print("")
        for indice,i in enumerate(self.Tabuleiro):
            print(f"{indice}  ",end="")
            for indice2, j in enumerate(i):
                print(f"{j}  ",end="")
            print("")

    def PosicionarCavalo(self):
        linha = int(input("Digite uma linha entre 0 ~ 7: "))
        while linha < 0 or linha > 7:
            linha = int(input("Linha invalida, digite uma nova: "))
        coluna = int(input("Digite uma coluna entre 0 ~ 7: "))
        while coluna < 0 or coluna > 7:
                    coluna = int(input("Coluna invalida, digite uma nova: "))
        self.LocCavalo = (linha,coluna)
        self.__EncontarCasas()
        os.system("cls")
        print("Gerando",end="")
        for i in range(3):
            time.sleep(.5)
            print(".",end="")
        print("\n")
        time.sleep(.5)
        self.PrintarTabuleiro()
        print("")
        input("Pressione enter para continuar")
        os.system("cls")


opcao = None
Tab = Tabuleiro()
while opcao != 0:
    os.system("cls")
    opcao = int(input("Gostaria de escolher uma casa para simular os movimentos?\n[0] Não\n[1] Sim\n> "))
    match opcao:
        case 0:
            break
        case 1:
            Tab.PosicionarCavalo()