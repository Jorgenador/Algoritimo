import math
raio = float(input("Digite o raio da sua esfra para calcular o volume:"))
volume = (4/3) * math.pi * (raio**3)
print(f"O volume da esfera é: {round(volume,3)}")