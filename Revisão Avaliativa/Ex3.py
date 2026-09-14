tarefas = {}
template = {"Concluida":False,"Desc":None}

def AdicionarTarefa():
    Tarefa = input("Digite o nome da tarefa: ")
    Descricao = input("Digite uma descricao para a tarefa: ")
    tarefas[Tarefa] = template.copy()
    tarefas[Tarefa]["Desc"] = Descricao

def RemoverTarefa():
    print(f"Escolha a tarefa para remover: {tarefas.keys()}")
    tarefa = input(">")
    del tarefas[tarefa] 

def ConcluirTarefa():
    print(f"Escolha a tarefa para Concluir: {list(tarefas.keys())}")
    tarefa = input("> ")
    tarefas[tarefa]["Concluida"] = True

def ExibirTarefas():
    print(tarefas)
    if not tarefas:
        print("Adicione uma tarefa para começar!")
        return
    print("-=-"*5)
    print("*** Tarefas Pendentes ***")
    for Tarefa in tarefas:
        print(Tarefa)
        if tarefas[Tarefa]["Concluida"] == False:
            print(f"Tarefa: {Tarefa}")
            print(f"Descrição: {tarefas[Tarefa]["Desc"]}")
    print("*** Tarefas Concluidas ***")
    for Tarefa in tarefas:
            if tarefas[Tarefa]["Concluida"] != False:
                print(f"Tarefa: {Tarefa}")
                print(f"Descrição: {tarefas[Tarefa]["Desc"]}")
    print("-=-"*5)



while True:
    Escolha = int(input("Escolha uma das opções \n[0] Sair \n[1] Adicionar Tarefa\n[2] Concluir Tarefa \n[3] Remover Tarefas\n[4] Listar Tarefas\n> "))
    match Escolha:
        case 0:
            break
        case 1:
            AdicionarTarefa()
        case 2:
            ConcluirTarefa()
        case 3:
            RemoverTarefa()
        case 4:
            ExibirTarefas()
        case _:
            print("Opção invalida, tente novamente.")