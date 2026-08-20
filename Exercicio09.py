alunos = {}

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):
    nome = input(f"Nome do aluno {i + 1}: ")
    nota = float(input(f"Nota de {nome}: "))
    alunos[nome] = nota

maior_nome = max(alunos, key=alunos.get)
maior_nota = alunos[maior_nome]

print(f"\nO aluno com a maior nota foi {maior_nome}, com nota {maior_nota}.")