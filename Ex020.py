from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lis = [a1, a2, a3, a4]
shuffle(lis)
print('A ordem de apresentação será:\n{}'.format(lis))