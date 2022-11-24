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