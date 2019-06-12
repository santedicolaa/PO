import random
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import itertools as it
mpl.use('Agg')

def geraListaAle(tam):
    lista = []
    for i in range(tam):
        lista.append(i)
    random.shuffle(lista)
    return lista

def geraListaCre(tam):
    lista = []
    for i in range(tam):
        lista.append(i)
    return lista

def geraListaDec(tam):
    lista = []
    n = tam
    for i in range(tam):
        lista.append(n)
        n -=1
    return lista

def Heap(lista, n, i): 
    maior = i
    esquerda = 2 * i + 1     
    direita = 2 * i + 2     
  
    if esquerda < n and lista[i] < lista[esquerda]: 
        maior = esquerda 
  
    if direita < n and lista[maior] < lista[direita]: 
        maior = direita 
  
    if maior != i: 
        lista[i],lista[maior] = lista[maior],lista[i]     
        Heap(lista, n, maior) 
  

def HeapSort(lista): 
    tam = len(lista) 
  
    for i in range(tam, -1, -1): 
        Heap(lista, tam, i) 
  
    for i in range(tam-1, 0, -1): 
        lista[i], lista[0] = lista[0], lista[i]
        Heap(lista, i, 0) 

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

PiorCaso = []
MelhorCaso = []
CasoAle = []

for i in x:
    lista = geraListaDec(i)
    PiorCaso.append(timeit.timeit('HeapSort({})'.format(lista),setup="from __main__ import HeapSort",number=1))
    
    lista = geraListaAle(i)
    CasoAle.append(timeit.timeit('HeapSort({})'.format(lista),setup="from __main__ import HeapSort",number=1))
    
    lista = geraListaCre(i)
    MelhorCaso.append(timeit.timeit('HeapSort({})'.format(lista),setup="from __main__ import HeapSort",number=1))

desenhaGrafico(x, PiorCaso, MelhorCaso, CasoAle, "graph_time.png")

lis = [1, 2, 3, 4, 5, 6]
permut = list(it.permutations(lis,6))
tempo = []
listaok = []

for i in permut:
  listaok.append(list(i))

for i in range(len(listaok)):
    tempo.append(timeit.timeit('HeapSort({})'.format(listaok[i]),setup="from __main__ import HeapSort",number=1))

maior = tempo.index(max(tempo))
menor = tempo.index(min(tempo))

print('Tempo maior:',max(tempo))
print(permut[maior])
print("\n")
print('Tempo menor:',min(tempo))
print(permut[menor])
