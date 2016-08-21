def ordenaSelecao(v):
    troca = 0
    n = len(v)
    for i in range(n):
        menor = i
        for j in range(i+1, n):
            if v[j] < v[menor]:
                menor = j
        aux = v[i]
        v[i] = v[menor]
        v[menor] = aux
        troca += 1
    print("Foram feitas %d trocas" % troca)
    return v

vetor = [20, 13, 17, -9, 4, 8, 2, -1, -5, 0, -11, 6]
print(vetor)
ordenaSelecao(vetor)
print(vetor)
