numero = float(input("Digite um número: "))

if numero < 0:
    print("Não existe raiz quadrada real de número negativo.")
else:
    chute = numero / 2 if numero != 0 else 0
    precisao = 0.0001

    while abs(chute * chute - numero) >= precisao:
        chute = (chute + numero / chute) / 2

    print(f"Raiz quadrada aproximada: {chute:.4f}")