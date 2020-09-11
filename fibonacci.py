print("Sequência de Fibonacci \n")
n=0
while n < 2:
    try:
        n = int(input("Digite n (>1): "))
        if n < 2:
            print ("Digite n >=2")
        
    except:
        print("O dado digitado deve ser um numero inteiro!")

#criação da lista da sequência de Fibonacci
l=[0,1]             
for i in range (n-2):
    l.append (l[i]+l[i+1])

print("Sequência gerada:", l)
print("Fim do programa")      
