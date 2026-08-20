numero = float(input("Digite um número para calcular a raiz quadrada:"))

chute = numero / 2
precisao = 0.0001

while abs(chute**2 - numero) >= precisao:
    chute = (chute + numero / chute) / 2

print("A raiz quadrada aproximada é:", round(chute, 4))