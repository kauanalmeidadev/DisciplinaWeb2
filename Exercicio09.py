alunos = {}

quantidade = int(input("Quantos alunos deseja cadastrar:"))

for i in range(quantidade):
    nome = input("Nome do aluno:")
    nota = float(input("Nota do aluno:"))
    alunos[nome] = nota

maior_nome = max(alunos, key=alunos.get)

print("O aluno com a maior nota foi:", maior_nome,"com nota", alunos[maior_nome])