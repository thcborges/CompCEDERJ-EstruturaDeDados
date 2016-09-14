class Lista:
    def __init__(self):
        self.chave = 0
        self.proximo = None


def insere_lista(elemento, prim):
    p = Lista()
    p.chave = elemento
    p.proximo = prim
    return p


def insere_depois(elemento, posicao, p):
    novo = Lista()
    novo.chave = elemento
    while p.chave != posicao:
        p = p.proximo
    novo.proximo = p.proximo
    p.proximo = novo
    return None


def insere_antes(elemento, posicao, p):
    novo = Lista()
    while p.chave != posicao:
        p = p.proximo
    novo.proximo = p.proximo
    p.proximo = novo
    novo.chave = p.chave
    p.chave = elemento
    return None


def remover(elemento, prim):
    seguinte, anterior = procura_valor(prim, elemento)
    if seguinte != None or anterior != None:
        if anterior == None:
            return anterior, seguinte.proximo

        elif seguinte.proximo == None:
            temp = seguinte
            anterior.proximo = seguinte.proximo
            return temp, prim

        else:
            temp = seguinte.chave
            aux = seguinte.proximo
            seguinte.chave = aux.chave
            seguinte.proximo = aux.proximo
            return temp, prim

    else:
        return "não existe na lista.", prim


def procura_valor(prim, elemento):
    p = prim
    q = None
    while p != None:
        if p.chave == elemento:
            return p, q
        q = p
        p = p.proximo
    return None, None


def imprime_lista(prim):
    print("========= L I S T A =========")
    p = prim
    while p != None:
        print(p.chave, end=" ")
        p = p.proximo
    print()
    print("=============================")


# Programa Principal
prim = None

for i in range(0, 7, 3):
    prim = insere_lista(i, prim)

imprime_lista(prim)

for j in range(1, 7, 3):
    insere_depois(j, j + 2, prim)

imprime_lista(prim)

for k in range(2, 7, 3):
    insere_antes(k , k - 1, prim)

imprime_lista(prim)

remove = int(input("Qual elemento deseja remover? (-1 - encerrar)\n"))
while remove != -1 and prim != None:
    removido, prim = remover(remove, prim)
    print("Valor removido", removido)
    imprime_lista(prim)
    remove = int(input("Qual elemento deseja remover? (-1 - encerrar)\n"))

imprime_lista(prim)

for valor in range(31):
    buscado, anterior = procura_valor(prim, valor)
    if buscado != None:
        print("Existe ", valor)
    else:
        print("Não existe ", valor)
