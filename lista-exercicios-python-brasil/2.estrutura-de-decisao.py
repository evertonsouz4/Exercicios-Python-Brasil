# 1.Faça um Programa que peça dois números e imprima o maior deles.
num_1 = int(input('Digite o 1° número: '))
num_2 = int(input('Digite o 2° número: '))

if num_1 > num_2:
    print(f'\nO 1° número é maior, sendo {num_1}')
elif num_1 == num_2:
    print('\nOs dois números são iguais')
else:
    print(f'\nO 2° número é maior, sendo {num_2}')