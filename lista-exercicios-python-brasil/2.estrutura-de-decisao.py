# 1.Faça um Programa que peça dois números e imprima o maior deles.
num_1 = int(input('Digite o 1° número: '))
num_2 = int(input('Digite o 2° número: '))

if num_1 > num_2:
    print(f'\nO 1° número é maior, sendo {num_1}')
elif num_1 == num_2:
    print('\nOs dois números são iguais')
else:
    print(f'\nO 2° número é maior, sendo {num_2}')

#2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = int(input('Digite um valor: '))
if valor >= 0:
        print('\nO valor digitado é positivo!')
else:
    print('\nO valor digitado é negativo!')

#3.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = str(input('Digite F ou M: '))
if sexo == 'F':
    print('F - Feminino.')
elif sexo == 'M':
    print('M - Masculino.')
else:
    print('Sexo Inválido.')

#4.Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
vogal_consoante = str(input('Digite uma letra: '))
if vogal_consoante == 'a' or vogal_consoante == 'e' or vogal_consoante == 'i' or vogal_consoante == 'u':
    print('\nA letra informada é uma vogal.')
else:
    print('\nA letra informada é uma consoante.')

#5.Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
    #A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    #A mensagem "Reprovado", se a média for menor do que sete;
    #A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota_1 = int(input('Digite sua nota parcial 1: '))
nota_2 = int(input('Digite sua nota parcial 2: '))
media = (nota_1 + nota_2)/2

print(f'\nSua nota média é de: {media}')

if media == 10:
    print('\nSua média foi 10, APROVADO COM DISTINÇÃO!')
elif media >= 7:
    print('\nSua média foi superior a 7, você está APROVADO!')
else:
    print('\nVocê foi reprovado, média menor que sete.')

#6.Faça um Programa que leia três números e mostre o maior deles.
num_1 = int(input('Digite um o 1° numero: '))
num_2 = int(input('Digite um o 2° numero: '))
num_3 = int(input('Digite um o 3° numero: '))

if num_1 > num_2 and num_1 > num_3:
    print(f'O 1° número é o maior, sendo: {num_1}')
elif num_2 > num_1 and num_2 > num_3:
    print(f'O 2° número é o maior sendo: {num_2}')
else:
    print(f'O 3° número é o maior sendo: {num_3}')