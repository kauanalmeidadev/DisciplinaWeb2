primos = []
numero = 2

while len(primos) < 10:
    eh_primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            eh_primo = False
            break
    if eh_primo:
        primos.append(numero)
    numero += 1

for p in primos:
    print(p)