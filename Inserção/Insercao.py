from Busca import BuscaLinear


def insere(x):
    x = int(x)
    v = BuscaLinear.v
    n = len(v)
    if BuscaLinear.busca1(x) < 0:
        v.append(x)
        n = n+1
    else:
        print("Elemento já existe na tabela")

