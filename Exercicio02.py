numero = int(input("Digite um número para verificar se é primo:"))

if numero > 1:
    for i in range(2, int(numero**0.5)+1):
        if (numero % i) == 0:
            print(numero,"não é um número primo.")
            break
        else:
            print(numero,"é um número primo.")
else:
    print(numero,"não é um número primo.")            