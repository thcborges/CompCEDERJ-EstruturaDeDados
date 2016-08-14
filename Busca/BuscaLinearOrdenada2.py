global v
v  = [0,9,16,24,38,43]

#Busca linear ordenada metodo 2
def busca_ord2(x):
    x = int(x)
    n = len(v)
    if x<=v[n-1]:
        i=0
        while v[i] < x:
            i = i +1
        if v[i] != x:
            busca_ord2 = -1
        else:
            busca_ord2 = i
    else:
        busca_ord2 = -1
    return busca_ord2


