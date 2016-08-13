from Busca import BuscaLinearOrdenada

def insereOrdenado(x):
    x = int(x)
    v = BuscaLinearOrdenada.v
    n = len(v)
    v.append(x) #SENTINELA
    i = 0
    while v[i] < x:
        i = i + 1
    if i < n+1 and v[i] != x:
        j = n
        for j in [i]:
            v[j+1] = v[j]
        v[i] = x
        n = n +1
    else:
        if i == n+1:
            n = n+1
        else:
            print("Elemento já exist na tabela")


