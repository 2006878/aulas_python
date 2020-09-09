#Definindo a Função
def f(x): #define a função
    "função que calcula o x ao quadradoe soma 1"
    res = x**2+1 #calcula e armazena em res
    print (res) #dessa forma usando print podemos apenas imprimir

def juros(preco,juros):
    res = preco*(1+(juros/100)) #calcula o preço multiplicado a uma taxa de juros 
    return res #dessa forma usando return podemos usar o resultado numa outra expressão por exemplo aritmética

#Testando a função
#print (f(4)) #imprime a função de 4
#print (f(10))
valor = input('Digite o valor a ser calculado: ')
juro = input('Digite a taxa de juros: ')
valor=eval(valor)
juro=eval(juro)

print (juros(valor,juro)) #imprime a função do valor 10 a juros de 50

