# 1.Faça um Programa que mostre a mensagem "Alô mundo" na tela. 
print('Alô Mundo!!!')

# 2.Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
num = int(input('Digite um numero: '))
print('O numero informado foi', num)

# 3.Faça um Programa que peça dois números e imprima a soma.
num_1 = int(input('Digite um numero: '))
num_2 = int(input('Digite um numero: '))
soma = num_1 + num_2
print(f'\nA soma entre os numeros e: {soma}')

# 4.Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print('Notas bimestrais\n')
nota_1 = int(input('Digite sua nota do 1° bimestre: '))
nota_2 = int(input('Digite sua nota do 2° bimestre: '))
nota_3 = int(input('Digite sua nota do 3° bimestre: '))
nota_4 = int(input('Digite sua nota do 4° bimestre: '))
media = (nota_1 + nota_2 + nota_3 + nota_4)/4

print(f'\nSua nota média bimestral é: {media}')

# 5. Faça um Programa que converta metros para centímetros.
print('Conversor de metros para centímetros\n')
metro = int(input('Digite um número em metros: '))
centimetro = metro * 100

print(f'O valor convertido é: {centimetro} centímetros.')
