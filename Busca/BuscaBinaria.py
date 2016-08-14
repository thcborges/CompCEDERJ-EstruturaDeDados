import math


def buscaBin(x, vetor, n):
    inf = 0
    sup = n - 1
    c = 0
    buscado = -1
    while inf <= sup:
        meio = math.floor((inf+sup)/2)
        if vetor[meio] == x:
            buscado = meio
            inf = sup + 1
        else:
            if vetor[meio] < x:
                inf = meio + 1
            else:
                sup = meio - 1
        c += 1
    print("Foram feitas %d comparações." % c, end="\n")
    return buscado

vetor = [1, 3, 6, 9, 10, 11, 15, 16, 19, 20, 22, 26, 28, 31, 33, 34]
x = int(input("Digite um valor a ser buscado: "))
posicao = buscaBin(x, vetor, len(vetor))

if posicao == -1:
    print("Número não encontrado.")
else:
    print("O número %d está na posição %d." % (x, posicao), end="\n")