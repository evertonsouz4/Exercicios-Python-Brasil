# 1.Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
vetor = []
for i in range(5):
    vetor.append(input('Adicione um número: '))
    print(vetor)

# 2.Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vetor = []
for i in range(10):
    vetor.append(input('Adicione um número: '))
    print(vetor[::-1])

# 3.Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
nota = []
media = 0
for i in range(4):
    nota.append(float(input('Digite a nota: ')))
    media += nota[i]
media = media / 4
print(nota)
print(media)