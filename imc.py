peso=eval(input('Digite seu peso: '))
altura=eval(input('Digite sua altura: '))
imc=peso/(altura*2)
print('Seu IMC é',imc)
if imc<18.8:
    print('Abaixo do peso')
elif imc>=25:
    print('Sobrepeso')
else:
    print('Normal')
