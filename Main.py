import os
import importlib
from pathlib import Path

def ImportarModulos():
    current_folder = Path(__file__).parent.resolve()
    ModulosInstanciados = {}
    for pastas in current_folder.iterdir():
        # Existem varios arquivos oculos aq, por isso essa checagem
        if pastas.name.startswith("."):
            continue

        if pastas.is_dir():
            ModulosInstanciados[pastas.name] = {}
            for module_arquiv in pastas.iterdir():
                if module_arquiv.is_file() and module_arquiv.suffix == ".py" and not module_arquiv.name.startswith("."):
                    nome_modulo = module_arquiv.stem
                    path_importar = f"{pastas.name}.{nome_modulo}"

                    ModuloImportado = importlib.import_module(path_importar)
                    ModulosInstanciados[pastas.name][nome_modulo] = ModuloImportado

    return ModulosInstanciados

modulos = ImportarModulos()
escolha = None

while escolha != 0:
    listaComPastas = list(modulos.keys())

    print("Listas disponiveis para executar exercicios:")
    print("[0] Sair")
    for i,nome_pasta in enumerate(modulos):
        print(f"[{i+1}] {nome_pasta}")
    escolha = int(input("Escolha a lista de exercicios: "))
    os.system('cls')
    if escolha == 0:
        break
    if 1 <= escolha <= len(listaComPastas):
        escolha2 = None
        while escolha2 != 0:
            print("Exercicios disponiveis para serem executados e suas descrições:")
            print("[0] Voltar")
            pastaSelecionada = listaComPastas[escolha-1]
            exerciciosDaPasta = modulos[pastaSelecionada]
            listaComExercicios = list(exerciciosDaPasta.keys())

            for i,nome_exercicio in enumerate(exerciciosDaPasta):
                print(f"[{i+1}] {nome_exercicio}",end="")
                if modulos[pastaSelecionada][nome_exercicio].desc:
                    print(f" Descrição: {modulos[pastaSelecionada][nome_exercicio].desc}")
                else:
                    print("")
            escolha2 = int(input("Escolha o Exercicio para ser executado: "))
            if escolha2 == 0:
                break
            if 1 <= escolha2 <= len(listaComExercicios):
                exSelecionado = listaComExercicios[escolha2-1]
                moduloRodar = exerciciosDaPasta[exSelecionado]

                print(f"Rodando: {exSelecionado}")
                moduloRodar.Init()
                input("Digite enter para continuar")
                os.system('cls')
            else:
                print("Opção invalida")
    else:
        print("Opção Invalida")


print("Encerrando!!")