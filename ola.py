'''line1 = "Olá desenvolvedor Python"
line2 = "Bem vindo ao mundo Python!"
nome = input('Digite seu primeiro nome: ')
sobrenome = input('Digite seu primeiro nome: ')
print ('Olá'+' '+nome+' '+sobrenome)
print (line2)

f= eval(input('Digite a temperatura em Farenheith:'))
celsius =(((f-32)/9)*5)
print ('A temperatura em graus Celsius é ',celsius)
if celsius>30:
    print ('Está muito quente, tome bastante liquido')
else:
    print ('Hoje está fresco')

print ('Adeus')
a = ['Tairone', 'Adriana', 'Ana Laura',  'Isabela']
nome = input('Digite seu nome para entrar: ')
if nome in a:
     print ('Você entrou')
else:
    print ('Usuário desconhecido')

for char in nome:
    print(char)
print ('Fim')'''

'''frase = input ('Digite uma frase: ')
for vogal in frase:
    if vogal in 'aeiouAEIOU':
     print (vogal)'''

print('Sequência de Fibonacci\n') # leitura do número de termos 
N = 0
while N<2:
 try:
  N = int(input('Digite N(>1): ')) 
  if N<2:
    print('Digite N >= 2') 
 except:
   print ('O dado digitado deve ser um número inteiro.')
A = 0 
B = 1
print('0, 1, ', end='') 
i = 0
while i < N-2: 
    C = A + B
    B = C 
    i += 1
print('\n\nFim do Programa') 