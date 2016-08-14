global v
v  = [0,9,16,24,38,43]

#Busca Linear
def busca1(x):
    x = int(x)
    i = 0
    busca1 = -1
    n = len(v)
    while i<= n-1:
        if v[i]==x:
            busca1 = i
            i = n
        else:
            i = i + 1
    return busca1


