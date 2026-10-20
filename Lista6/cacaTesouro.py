import random
import time
import os
desc = "Caça ao tesouro com POO"
class Matriz:
    def GerarMatriz(self):
        matriz = [[False for j in range(self.tamanho)] for i in range(self.tamanho)]
        self.cordTesouro = (random.randint(0,self.tamanho-1),random.randint(0,self.tamanho-1))
        matriz[self.cordTesouro[0]][self.cordTesouro[1]] = True
        self.Matriz = matriz

    def CalcularDistancia(self,chuteLinha,ChuteColuna):
        distanciaLinha = abs(self.cordTesouro[0] - chuteLinha)
        distanciaColuna = abs(self.cordTesouro[1] - ChuteColuna)
        distancia = max(distanciaLinha,distanciaColuna)
        txt = None
        if distancia > 3:
            txt = "Longe"
        elif distancia in [2,3]:
            txt = "Perto"
        else:
            txt = "Muito Perto"
        return txt
    
    def __init__(self,):
        self.tamanho = int(input("Escolha o tamanaho da matriz (Ex: 5 = 5x5, 6 = 6x6)\n> "))  
        self.GerarMatriz()
        self.Tentativas = []
        self.Vitoria = False

    def PrintarMatriz(self):
        print("  ",end="")
        for i in range(self.tamanho):
            print(f" {i}  ",end="")
        print()
        for indice,i in enumerate(self.Matriz):
            print(f"{indice} ",end="")
            for indice2,i2 in enumerate(i):
                if (indice,indice2) == self.cordTesouro and self.cordTesouro in self.Tentativas:
                    print(f"|✔| ",end="")
                elif ((indice,indice2)) in self.Tentativas:
                    print(f"|X| ",end="")
                else:
                    print(f"|?| ",end="")
            print()

    def Jogar(self):
        print(f"Vamos começar! a sua matriz é de tamanho {self.tamanho}x{self.tamanho}: ")
        while not self.Vitoria:
            self.PrintarMatriz()
            print("Caso queira desisitr, digite -1")
            linha = int(input("Digite a linha para cavar: "))
            while linha > (self.tamanho-1) or linha < -1:
                linha = int(input("Muito grande, digite uma nova linha para cavar: "))
            if linha == -1: break
            coluna = int(input("Digita a coluna para cavar: "))
            while coluna > (self.tamanho-1) or coluna < -1:
                coluna = int(input("Muito grande, digite uma nova coluna para cavar: "))
            if coluna == -1: break
            print(f"Cavanado nas cordenadas ({linha},{coluna})",end="")
            for i in range(3):
                time.sleep(0.5)
                print(".",end="")
            print()
            self.Tentativas.append((linha,coluna))
            if (linha,coluna) != self.cordTesouro:
                print("Você não achou nada...")
                distancia = self.CalcularDistancia(linha,coluna)
                if distancia in ["Perto","Muito Perto"]:
                    print(f"Não desanime você está {distancia}")
                else:
                    print(f"Você está {distancia}")
            else:
                print("Você achou o tesouro!!")
                self.Vitoria = True
            time.sleep(.5)
            input("Pressione enter para continuar")
            os.system("cls")

    def Historico(self):
        if self.Vitoria == True:
            print("Essa partida terminou em vitoria!")
            time.sleep(1)
            print(f"Foram necessarios {len(self.Tentativas)} tentativas para alcançara vitoria.")
            time.sleep(1)
            print("Esse é o mapa após suas tentativas")
            time.sleep(1)
            self.PrintarMatriz()
        else:
            print("Essa partida foi uma derrota")
            time.sleep(1)
            print(f"Você desisitu após {len(self.Tentativas)} tentativas")
            time.sleep(1)
            print("Esse é o seu mapa após suas tentativas")
            time.sleep(1)
            self.PrintarMatriz()
        input("Pression enter para continuar")
        os.system("cls")

def Init():
    partidas = []

    escolha = None
    while escolha != 0:
        escolha = int(input("Como gostaria de prosseguir?\n[0] Sair\n[1] Iniciar caça ao tesouro\n[2] Historico de partidas\n> "))
        match escolha:
            case 0:
                break
            case 1:
                matriz = Matriz()
                matriz.Jogar()
                partidas.append(matriz)
            case 2:
                if len(partidas) == 0: print("Nenhuma partida jogada ainda"); continue
                consultar = int(input(f"Você jogou {len(partidas)} partidas, qual delas você gostaria de consultar?\n>"))
                if consultar >= 1 and consultar <= len(partidas):
                    partida = partidas[consultar-1]
                    partida.Historico()
                else:
                    print("Partida invalida.")