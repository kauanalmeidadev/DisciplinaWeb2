numero_perfeito = int(input("Digite um número inteiro positivo:"))

soma_divisores = sum(i for i in range (1, numero_perfeito) if numero_perfeito % 1 == 0)

if soma_divisores == numero_perfeito and numero_perfeito > 0:
    print(numero_perfeito,"é um número perfeito.")
else:
    print(numero_perfeito,"Não é um número perfeito.")    