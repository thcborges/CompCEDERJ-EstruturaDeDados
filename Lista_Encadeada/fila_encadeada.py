class PT:
    def __init__(self):
        self.valor = 0
        self.anterior = None
        self.proximo = None


def insere_fila(novo_valor, primeiro, ultimo):
    novo = PT()
    novo.valor = novo_valor

    if ultimo == None:
        primeiro = novo
    else:
        ultimo.proximo = novo

    novo.anterior = ultimo
    novo.proximo = None

    ultimo = novo

    return primeiro, ultimo

def remove_fila(primeiro, ultimo):
    if primeiro == None:
        return "Fila vazia", primeiro, ultimo

    saida = primeiro
    q = primeiro.proximo

    if q == None:
        ultimo = None
    else:
        q.anterior = None

    primeiro = q

    return saida.valor, primeiro, ultimo


def imprime_fila(primeiro):
    print("----------- F I L A ----------")
    p = primeiro
    while p != None:
        print(p.valor, end=" ")
        p = p.proximo
    print()
    print("------------------------------")


primeiro = None
ultimo = None
mensagem = "O que deseja fazer?\n1 - Entrar na fila\n2 - Sair da fila\n0 - Encerrar\n\n"
acao = int(input(mensagem))
cliente = 1
while acao != 0:
    if acao == 1:
        primeiro, ultimo = insere_fila(cliente, primeiro, ultimo)
        cliente += 1
    else:
        retirado, primeiro, ultimo = remove_fila(primeiro,ultimo)
        print("Cliente atendido: ", retirado)

    imprime_fila(primeiro)
    acao = int(input(mensagem))
