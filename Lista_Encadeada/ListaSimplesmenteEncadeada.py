#adicionarei comentários ao lado demonstrando onde há um ponteiro
class Lista:
    def __init__(self):
        self.chave = 0
        self.prox = None


def percurso(ptlista):
    pont = Lista()
    pont = ptlista  # ptlista^ ==> ptlista^.prox vai despresar o primeiro elemento
    while pont != None:
        visita(pont.chave)  # pont^.info
        pont = pont.prox  # pont^.prox
    return None


def visita(pont):
    print(pont, end=" ")
    return None


def busca_end_ord(x, ptlista):  # adicionando ptlista a passagem de parametros || pont e ent não precisam ser passados
                                # como parametro, pois são alterados já no inicio da busca, porém são retornados
    ant = ptlista
    pont = None
    ptr = ptlista.prox  # ptr -> ponteiro de percurso || ptlista^.prox
    while ptr != None:
        if ptr.chave < x:  # ptr^.chave
            ant = ptr
            ptr = ptr.prox  # ptr^.chave
        elif ptr.prox == x:  #ptr^.chave
            pont = ptr
        ptr = None

    return pont, ant


# Minha reposta para o exercício 1 da aula 13
def busca_end(x, ptlista):
    ant = None
    ptr = ptlista
    while ptr != None and ptr.chave != x:
        ant = ptr
        ptr = ptr.prox
    return ptr, ant


# resposta exercício
def busca_enc_nao_ord(x, ptlista):  # novamente, pont e ant não precisa ser passado como parametro, precisam ser retornados
    ant = ptlista  # O correto seria usar None
    pont = None
    ptr = ptlista  # Se eu utilizar o ptlista^.chave despresarei o primeiro elemento da lista
    while ptr != None:
        if ptr.chave == x:  # ptr^chave ==> chave encontrada
            pont = ptr  # p
            ptr = None
        else:
            ant = ptr
            ptr = ptr.prox
    return pont, ant



# Minha resposta para o exercício 2 aula 13
class Matriz:
    def __init__(self):
        self.chave = None
        self.coluna = None
        self.linha = None
        self.proximo = None


def aloca_matriz(matriz):
    mat = Matriz()
    aux = mat
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if matriz[l][c] != 0:
                aux.chave = matriz[l][c]
                aux.linha = l
                aux.coluna = c
                aux = mat.proximo
    return mat


# Exercício final
def imprime_inverso(ptlista):
    p = ptlista
    topo = None
    while p != None:
        pilha = Lista()
        pilha.chave = p.chave
        pilha.prox = topo
        topo = pilha
        p = p.prox
    print("===========================================================================================================")
    q = topo
    while q != None:
        print(q.chave, end=" ")
        q = q.prox
    print()
    print("===========================================================================================================")


def insere_lista(elemento, prim):
    p = Lista()
    p.chave = elemento
    p.prox = prim
    return p


lista = None
for chave in range(1, 51):
    lista = insere_lista(chave, lista)
imprime_inverso(lista)
percurso(lista)