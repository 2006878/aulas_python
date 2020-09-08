'''a = eval(input('Digite o lado A:'))
b = eval(input('Digite o lado B:'))
c = eval(input('Digite o lado C:'))

maior_lado = 0
if (a>maior_lado):
    maior_lado = a
if (b>maior_lado):
    maior_lado = b
if (c>maior_lado):
    maior_lado = c

maior_lado = max(a,b,c)

if (maior_lado<a+b+c-maior_lado):
    print('Os lados formam um triângulo')
    if a==b and b==c and a==c:
        print('Triângulo Equilátero')
    elif a!=b and b!=c and a!=c:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
else:
    print('Os lados não formam um triângulo')
    '''
temp = eval(input('Digite a temperatura:'))
if temp>86:
    print('Quente')
elif temp>32:
    print('Frio')
else:
    print('Congelando')        
