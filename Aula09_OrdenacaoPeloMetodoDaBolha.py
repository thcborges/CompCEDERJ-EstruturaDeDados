def ordenaBolha(v, n):
    troca = 0
    for i in range(n):
        bolha = i
        while bolha > 1:
            if v[bolha] < v[bolha-1]:
                aux = v[bolha-1]
                v[bolha-1] = v[bolha]
                v[bolha] = aux
                bolha = bolha -1
                troca += 1
            else:
                bolha = 1
    print("Foram feitas %d trocas" % troca, end="\n")


vetor = [20, 13, 17, -9, 4, 8, 12]
print(vetor)
vetor = ordenaBolha(vetor, len(vetor))
print(vetor)