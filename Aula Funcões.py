#Definindo a Função
def f(x): #define a função
    "função que calcula o x ao quadrado e soma 1"
    res = x**2+1 #calcula e armazena em res
    print (res) #dessa forma usando print podemos apenas imprimir

def juros(preco,juros):
    res = preco*(1+(juros/100)) #calcula o preço multiplicado a uma taxa de juros 
    return res #dessa forma usando return podemos usar o resultado numa outra expressão por exemplo aritmética

#Testando a função
print (f(4)) #imprime a função de 4
print (f(10))

print (juros(10,50)) #imprime a função do valor 10 a juros de 50
