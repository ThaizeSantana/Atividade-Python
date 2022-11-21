# 4-  Utilizando condicionais:
# 4.1 Os alunos do PdA estão sendo avaliados, para passar para o próximo ciclo, deverão tirar, no mínimo, 7 na média.
# -Se o aluno tirar maior ou igual a 7 ele está aprovado.
# -Se o aluno tiver nota 6 e for participativo, irá para recuperação.
# -Senão, será reprovado.
# Faça um algoritmo que auxilie a avaliar a nota dos alunos.

nota=int(input('Qual sua nota?'))
if nota >=7:
    print('Você foi aprovado!')
elif nota == 6:
  print ('Você foi aprovado por ser participativo!')
else: 
  print ('Você foi reprovado!')
