import replit
import time

class Grafo():

  def __init__(self):
    self.inicio = {}
    self.num_vertices = 0
    self.lis_vertices = []
    
  def addVertice(self, vertice):
    inicio = self.inicio
    if vertice in inicio:
      print(vertice,"já pertence ao grafo")
      time.sleep(1)
      return 0
    if vertice not in inicio:
      inicio[vertice]={}
    self.num_vertices = self.num_vertices +1
    self.lis_vertices.append(vertice)

  def addCaminho(self, v1, v2, peso):
    inicio = self.inicio
    if v1 not in inicio:
      return 0

    if v2 not in inicio:
      return 0

    inicio[v1][v2]=peso
    inicio[v2][v1]=peso
    return 1

  def procurar(self, vertice):
    inicio = self.inicio
    if vertice in inicio:
      print("\nO vértice",vertice,"pertence ao grafo.\n")
      print("Adjacências e pesos:\n")
      for j in grafo.inicio[vertice]:
        print("    ", j, ", peso:",grafo.inicio[vertice][j])
      print("\n")
    else:
      print("\n", vertice, "não pertence ao grafo.\n")


grafo = Grafo()

def menu():
  replit.clear()
  print("*** Grafos ***\n")
  print("1 - Adicionar vértice")
  print("2 - Adicionar caminho")
  print("3 - Mostrar grafo")
  print("4 - Procurar Vértice\n")
  print("Escolha uma opção: ",end='')
  escolha = int(input())

  if escolha == 1:
    replit.clear()
    print("Nome do vértice: ",end='')
    nome = (input())
    grafo.addVertice(nome)
    print("\n",nome,"adicionado com sucesso!")
    time.sleep(1)
    menu()

  if escolha == 2:
    replit.clear()
    print("\nVértice de origem: ",end='')
    v1 = (input())
    print("\nVértice de destino: ",end='')
    v2 = (input())
    print("\nPeso do Caminho: ",end='')
    peso = (input())
    if(grafo.addCaminho(v1, v2, peso)):
      print("\nCaminho adicionado com sucesso!")
      time.sleep(1)
      menu()
    else:
      print("\nVértice inexistente.")
      time.sleep(1)
      menu()

  if escolha == 3:
    replit.clear()
    for i in grafo.lis_vertices:
      print("-",i,":")
      for j in grafo.inicio[i]:
        print("    ", j, ", peso:",grafo.inicio[i][j])
      print("\n")
    print("Digite algo para voltar ao menun principal: ", end='')
    if(input()):
      menu()

  if escolha == 4:
    replit.clear()
    print("\nVértice a ser procurado: ",end='')
    grafo.procurar(input())
    print("Digite algo para voltar ao menun principal: ", end='')
    if(input()):
      menu()

grafo = Grafo()
menu()
