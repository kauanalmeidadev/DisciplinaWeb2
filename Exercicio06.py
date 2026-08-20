primos = []
numero = 2

while len(primos) < 10:
    primo = True
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            primo = False
            break
    if primo:
        primos.append(numero)
    numero += 1

print("Primeiros 10 números primos:", primos)