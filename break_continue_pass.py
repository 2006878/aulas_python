#break
def primo(num):
    i = 2
    while i < num:
        if num % 1 == 0:
            break
        i += 1
    return i == num   

#continue
for n in range(2,100):
    if not primo(n):
        continue
    print(n)

#pass
if n % 2 == 0:
    pass
else:
    print(n)    