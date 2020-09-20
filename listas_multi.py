def simetrica(n):
    nlinhas = len(m)
    ncolunas = len(m[0])

    for i in range(nlinhas):
        for j in range (i+1, ncolunas):
            if m[i][j] != m[j][i]:
                return False
    return True

def print2d(m):
    for linha in m:
        for item in linha:
            print(item, end=' ')
        print()

#exemplo de lista unidimensional:
i=[1,2,3]
#lista bidimensional:
n=[[1,2,3],[4,5,6],[7,8,9]]
print('unidimensional=',i)
print('bidimensional=',n)
print(n[0][1])

m = [[1,2,3],[2,4,5],[3,5,3]]
print(simetrica(m))
for linha in m:
    print(linha) 
    print2d(m)