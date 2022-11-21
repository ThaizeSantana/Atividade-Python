# DESAFIO_01 = Estamos com dificuldade em identificar se um número é positivo, negativo ou neutro.
# Faça uma programa que imprima se o número é positivo, neutro ou negativo.

number = int(input('Insira um  número: '))
if number >0:
    print('Número positivo!')
elif number ==0:
    print('Número neutro!')
else:
    print('Número negativo!')