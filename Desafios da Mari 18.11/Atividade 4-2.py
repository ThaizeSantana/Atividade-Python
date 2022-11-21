# 4.2 A PDA quer verificar se o Tiago está qualificado para tirar férias. 
# Para estar em condições, os seguintes requisitos devem ser satisfeitos:
# - Ter trabalhado no mínimo 12 meses completos.
# - Ter disponibilidade de tirar férias entre dezembro e janeiro.
# Faca um algoritmo que valide ou não essas duas opções para saber se o Tiago pode tirar férias. 
# O programa deverá escrever a mensagem “Tiago pode sair de férias “ ou  “Tiago não pode sair de férias”.

meses=int(input('Quantos meses o Tiago trabalhou?'))
if meses >=12:
    print('Tiago pode tirar férias!')
elif meses == 11:
  print ('Tiago não pode tirar férias, aos menos que  ele trabalhar mais 1 mês ')
else: 
  print ('Sem férias!')


