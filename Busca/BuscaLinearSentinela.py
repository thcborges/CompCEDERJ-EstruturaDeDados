global v
v  = [0,9,16,24,38,43]



#Busca com Sentinelas
def busca2(x):
    x = int(x);
    i = 0;
    busca2 = 0;
    v.append(x); #SENTINELA
    n = len(v)
    while v[i] != x:
        i = i + 1
    if i != n-1:
        busca2 = i
    else:
        busca2 = -1
    return busca2



print('Indice =', busca2(input()))

