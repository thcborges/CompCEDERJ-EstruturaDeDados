class PT:
    def __init__(self):
        self.valor = 0
        self.proximo = None


def empilha(novo_valor, topo):
    pt = PT()
    pt.valor = novo_valor
    pt.proximo = topo
    topo = pt
    return topo


def desempilha(topo):
    if topo != None:
        saida = topo.proximo
        return saida
    else:
        return None


def imprime_pilha(topo):
    print("---------PILHA----------")
    p = topo
    while p != None:
        print(p.valor, end=" ")
        p = p.proximo
    print()
    print("------------------------")


topo = None
mensagem = "O que deseja fazer?\n 0 - encerrar\n 1 - empilhar\n 2 - desempilhar\n"
acao = int(input(mensagem))
pilha = 1
while acao != 0:
    if acao == 1:
        topo = empilha(pilha, topo)
        pilha += 1
    elif acao == 2:
        topo = desempilha(topo)
        print("Retirado da pilha: ", topo)

    imprime_pilha(topo)
    acao = int(input(mensagem))