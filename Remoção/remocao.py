from Busca import BuscaLinear

def remove(x):
    v = BuscaLinear.v
    n = len(v)
    if n==0:
        print("Underflow")
    else:
        j = BuscaLinear.busca1(x)
        if j==0:
            print("O elemento não está na tabela")
        else:
            i = j
            while i < n-1:
                v[i] = v[i+1]
                i = i +1






print(BuscaLinear.v)
remove(9)
print(BuscaLinear.v)