# 1.Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    nota = int(input('Digite uma nota entre 0 e 10: '))
    if nota < 0 or nota > 10:
        print('Nota inválida!')
    else:
        print('Nota válida!') 
        break
           
# 2.Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    loguin = input('Informe um nome de usuario: ')
    senha = input('Informe uma senha: ')
    if loguin == senha:
        print('Erro! Não é permitido senha igual o loguin.')
        print('Digite loguin e senha novamente.\n')
    else:
        print('Cadastro concluído!')
        break
# 3.Faça um programa que leia e valide as seguintes informações: Nome maior que 3 caracteres, Idade entre 0 e 150, Salário maior que zero, sexo f ou m, Estado Civil 's', 'c', 'v', 'd'.
nome = input('Digite um nome: ')
idade = int(input('Digite uma idade: '))
salario = float(input('Digite seu sálario: '))
sexo = input('Digite seu sexo: ')
estado_civil = input('Digite seu estado civil: ')

if len(nome) <= 3:
    print('Erro! Nome deve ser maior que 3 caracteres.')
else:
    if idade < 0 or idade > 150:
        print('Erro! Idade deve está entre 0 e 150.')
    else:
        if salario <0:
            print('Erro! Salário deve ser maior que 0.')
        else:
            if sexo != 'f' and sexo != 'm':
                print('Erro! Sexo deve ser f ou m.')
            else:
                if estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
                    print("Erro! Estado civil deve ser: 's', 'c', 'v', 'd'")
                
