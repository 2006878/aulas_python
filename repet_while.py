'''num = eval(input('Digite um número positivo: '))
while num < 0:
    num = eval(input('Digite um número positivo: '))

l = []
nome = input('Digite um nome: ')
while nome != '':
    l.append(nome) #adiciona o nome na lista
    nome = input('Digite um nome: ')

for i in l:
    print(i)

print ("Início do programa")
cont=1
limite=eval(input('Digite o limite: '))
while cont <= limite:
    print (cont)
    cont = cont+1
print ("Fim do programa")'''

x=1
while x != 0:
    x=eval(input("Digite o valor de x: "))
    if x % 2 == 0:
        print(x," é par")
    else:
        print(x," é impar")    
