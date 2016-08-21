def ordenaBolha(v):
    troca = 0
    n = len(v)
    for i in range(n):
        bolha = i
        while bolha > 0:
            if v[bolha] < v[bolha-1]:
                aux = v[bolha-1]
                v[bolha-1] = v[bolha]
                v[bolha] = aux
                bolha -= 1
                troca += 1
            else:
                bolha = 0
    print("Foram feitas %d trocas" % troca)


vetor = [20, 13, 17, -9, 4, 8, 12]
print(vetor)
ordenaBolha(vetor)
print(vetor)