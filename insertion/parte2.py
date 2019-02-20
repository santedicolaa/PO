import itertools as it
from random import randint

def geraListaAle(tam):
  lista = []
  while tam > len(lista):
    for i in range(tam):
      n = randint(1,1*tam)
      if n not in lista: lista.append(n)
  return lista

def insertionSort(lista):
    i = 1
    swap = 0
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
            swap += 1

        i += 1
    return swap

lis_ale = geraListaAle(6)
lis_permut = list(it.permutations(lis_ale,6))
lis = []
lis_aux = []
swaps = []

for i in lis_permut:
    lis.append(list(i))
    lis_aux.append(list(i))

for j in range (len(lis)):
    swaps.append(insertionSort(lis[j]))

print("Piores casos:")

for k in range (len(swaps)):
    if swaps[k]==5:
        print(lis_aux[k], end = "\n")

print("\n")

print("Melhores casos:")

for k in range (len(swaps)):
    if swaps[k]==0:
        print(lis_aux[k], end = "\n")
