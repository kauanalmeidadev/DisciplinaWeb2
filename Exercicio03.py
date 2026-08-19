numero_str = input("Digite um número inteiro:")

soma_quadrados = sum(int(digito) ** 2 for digito in numero_str if digito.isdigit())

print("A soma dos quadrados dos digitos é:", soma_quadrados)
