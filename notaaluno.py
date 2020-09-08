n1=input('Digite a Nota 1: ')
n2=input('Digite a Nota 2: ')
n1=eval(n1)
n2=eval(n2)
media = 0.4*n1+0.6*n2
print('Sua média é:', media)
if (media>=5):
    print('Você foi aprovado com nota', media)
else:
    print('Você foi reprovado com nota', media)    