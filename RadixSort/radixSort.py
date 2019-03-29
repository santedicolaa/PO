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

def countingSort(arr, exp1): 
  n = len(arr) 
  count = []
  output = []

  for i in range (len(arr)):
    output.append(0)

  for i in range (n):
    count.append(0)

  for i in range(0, n): 
    index = (arr[i]/exp1) 
    count[int(index%10)] += 1

  for i in range(1,10): 
    count[i] += count[i-1] 

  i = n-1
  while i>=0: 
    index = (arr[i]/exp1) 
    output[count[int(index%10)] - 1] = arr[i] 
    count[int(index%10)] -= 1
    i -= 1

  i = 0
  for i in range(0,len(arr)): 
    arr[i] = output[i]
  
def radixSort(arr): 
  max1 = max(arr) 
  exp = 1
  while max1/exp > 0: 
    countingSort(arr,exp)
    exp *= 10

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
    PiorCaso.append(timeit.timeit('radixSort({})'.format(lista),setup="from __main__ import radixSort",number=1))
    
    lista = geraListaAle(i)
    CasoAle.append(timeit.timeit('radixSort({})'.format(lista),setup="from __main__ import radixSort",number=1))
    
    lista = geraListaCre(i)
    MelhorCaso.append(timeit.timeit('radixSort({})'.format(lista),setup="from __main__ import radixSort",number=1))

desenhaGrafico(x, PiorCaso, MelhorCaso, CasoAle, "graph_time.png")

lis = [1, 2, 3, 4, 5, 6]
permut = list(it.permutations(lis,6))
tempo = []
listaok = []

for i in permut:
  listaok.append(list(i))

for i in range(len(listaok)):
    tempo.append(timeit.timeit('radixSort({})'.format(listaok[i]),setup="from __main__ import radixSort",number=1))

maior = tempo.index(max(tempo))
menor = tempo.index(min(tempo))

print('Tempo maior:',max(tempo))
print(permut[maior])
print("\n")
print('Tempo menor:',min(tempo))
print(permut[menor])
