#Loops aninhados

list = ['João', 'Roberto' , 'Rafael']
for nome in list:
    print(nome)
    for c in nome:
        if c in 'aeiou':
            print(c)