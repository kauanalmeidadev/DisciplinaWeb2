texto = input("Digite um texto:")

vogais = "aeiouAEIOU"
resultado = ""

for letra in texto:
    if letra in vogais:
        resultado += "A"
    else:
        resultado += letra

print("Texto com vogais trocadas por A:", resultado)