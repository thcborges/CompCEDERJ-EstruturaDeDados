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
    anterior = prim
    seguinte = prim
    if procura_valor(prim, elemento):
        while seguinte.chave != elemento and seguinte.proximo != None:
            anterior = seguinte
            seguinte = seguinte.proximo
        if anterior.proximo == None:
            return anterior.chave, None
        if seguinte.proximo == None:
            temp = seguinte.chave
            anterior.proximo = seguinte.proximo
            return temp, prim
        elif anterior.proximo == None:
            print("anterior.proximo")
            temp = anterior.chave
            anterior.proximo = None
            anterior.chave = None
            return temp, None
        else:
            aux = Lista()
            temp = seguinte.chave
            aux = seguinte.proximo
            seguinte.chave = aux.chave
            seguinte.proximo = aux.proximo
            return temp, prim

    else:
        return  "não existe na lista.", prim


def procura_valor(prim, elemento):
    p = prim
    while p != None and p.chave != elemento:
        if p.chave == elemento:
            achou = True
        else:
            p = p.proximo
    if p != None:
        return True
    else:
        return False


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

for i in range(0, 31, 3):
    prim = insere_lista(i, prim)

imprime_lista(prim)

for j in range(1, 31, 3):
    insere_depois(j, j + 2, prim)

imprime_lista(prim)

for k in range(2, 31, 3):
    insere_antes(k , k - 1, prim)

imprime_lista(prim)

remove = int(input("Qual elemento deseja remover? (-1 - encerrar)\n"))
while remove != -1:
    removido, prim = remover(remove, prim)
    print("Valor removido", removido)
    imprime_lista(prim)
    remove = int(input("Qual elemento deseja remover? (-1 - encerrar)\n"))

imprime_lista(prim)

for valor in range(31):
    if procura_valor(prim, valor):
        print("Existe ", valor)
    else:
        print("Não existe ", valor)
