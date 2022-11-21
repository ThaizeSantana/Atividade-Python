# DESAFIO_02 = Precisamos identificar a menor média de um aluno para saber se ele pode seguir para a próxima fase de um projeto.
# Faça um programa que peça as três notas do aluno e imprima a menor deles.

(__:=[], [__.append(int(input(f'Insira a média {_ + 1}: '))) 
for _ in range(3)], print(f'A menor média do aluno é {min(__)}'))