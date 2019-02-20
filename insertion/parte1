from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('Agg')

def geraListaCre(tam):
    lista = []
    n = 1
    while tam > len(lista):
        for i in range(tam):
            lista.append(n)
            n += 1
    return lista

def geraListaDec(tam):
    lista = []
    n = tam
    while tam > len(lista):
        for i in range(tam):
            lista.append(n)
            n -= 1
    return lista

def geraListaAle(tam):
  lista = []
  while tam > len(lista):
    for i in range(tam):
      n = randint(1,1*tam)
      if n not in lista: lista.append(n)
  return lista

def insertionSort(lista):
    i = 1
    while i < len(lista):
        temp = lista[i]
        trocou = False
        j = i - 1
        while j >= 0 and lista[j] > temp:
            lista[j + 1] = lista[j]
            trocou = True
            j -= 1

        if trocou:
            lista[j + 1] = temp

        i += 1

def desenhaGrafico(x, pc, mc, ae, name, xl = "Entradas", yl = "Tempo (s)"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, pc, label = "Pior Caso")
    ax.plot(x, mc, label="Melhor Caso")
    ax.plot(x, ae, label="Aleatório")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name)

x = [10000, 20000, 30000, 40000, 50000]
melhor = []
pior = []
aleatorio = []

for i in range (len(x)):
    listaCresc = geraListaCre(x[i])
    listaDec = geraListaDec(x[i])
    listaAle = geraListaAle(x[i])
    melhor.append(timeit.timeit("insertionSort({})".format(listaCresc), setup="from __main__ import insertionSort", number=1))
    pior.append(timeit.timeit("insertionSort({})".format(listaDec), setup="from __main__ import insertionSort", number=1))
    aleatorio.append(timeit.timeit("insertionSort({})".format(listaAle), setup="from __main__ import insertionSort", number=1))


desenhaGrafico(x, pior, melhor, aleatorio, "graph_time.png")
