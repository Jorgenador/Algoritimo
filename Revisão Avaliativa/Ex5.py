Salario = float(input("Digite o valor do salario para ser calculado o imposto relativo ao valor.\n> "))
inss = None
irpf = None
if Salario <= 1500:
    inss = 0.925
elif Salario > 1500 and Salario < 3000:
    inss = 0.91
else:
    inss = 0.88

if Salario <= 2000:
    irpf = 1
elif Salario > 2000 and Salario <= 4000:
    irpf = 0.925
else:
    irpf = 0.85

SalarioPosTaxas = (Salario*inss)*irpf
print(f"Salario após descontos: {SalarioPosTaxas}")