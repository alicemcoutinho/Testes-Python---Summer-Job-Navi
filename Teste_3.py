id = {}

for i in range(5):
   aluno = input('Nome do(a) Aluno(a): ')
   grade = float(input('Nota: '))
   id[aluno] = grade

aluno_max = max(id, key = id.get)

print("O(a) aluno(a) de maior nota foi", aluno_max,"com nota", id[aluno_max])
