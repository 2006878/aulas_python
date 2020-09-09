num = eval(input('Digite um número positivo: '))
while num < 0:
    num = eval(input('Digite um número positivo: '))

l = []
nome = input('Digite um nome: ')
while nome != '':
    l.append(nome) #adiciona o nome na lista
    nome = input('Digite um nome: ')

for i in l:
    print(i)