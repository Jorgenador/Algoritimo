desc = "Consultar cpf"

def BuscarCpf(Lista,Chave):
    iteracoes = 1
    for i in Lista:
        if i == Chave:
            return iteracoes
        iteracoes+=1
    return -1

lista = [11111111101,16641295502,21341202592]
cpf = int(input("Digite o seu cpf: "))
iteracoes = BuscarCpf(lista,cpf)
if iteracoes != -1:
    print(f"CPF encontrado, {iteracoes} verificacoes até encontrar")
else:
    print("Cpf não encotrado")