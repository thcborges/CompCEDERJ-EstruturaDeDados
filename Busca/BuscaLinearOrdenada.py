global v
v  = [0,9,16,24,38,43]


#Busca linear ordenada
def busca_ord(x):
    x = int(x);
    i = 0;
    busca_ord = -1
    v.append(x) #SENTINELA
    n = len(v)
    while v[i]<x:
        i = i + 1
    if i<n-1 and v[i]==x:
        busca_ord = i
    return busca_ord;


