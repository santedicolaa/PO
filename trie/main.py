import replit
import time

class Trie(object):
  raiz = {}

  def adicionar(self, string):
    atual = self.raiz
    for char in string:
        if char not in atual:
            atual[char] = {}
        atual = atual[char]
    atual['*'] = True
    print("\n'", string,"' foi adicionada")

  def pesquisar(self, string):
    atual = self.raiz

    for char in string:
        if char not in atual:
            return False
        atual = atual[char]
    if '*' in atual:
        print("\n'",string,"' foi encontrada")
    else:
        print("\n'",string,"' não foi encontrada")

  def remover(self, string):
    nome = string
    atual = self.raiz
    if self.pesquisar(string) == False:
      print("\n'",string,"' não foi encontrada, portanto não pode ser removida")
      time.sleep(2)
      return False
    
    for i in string:
      atual = atual[i]
    del atual['*']

    while(len(string) > 0):
      atual = self.raiz
      for i in string:
        atual = atual[i]

      for k in atual:
        if atual[k]:
          break
      string = string[:-1]

    print("\n'", nome ,"' foi removida")

def menu():
  replit.clear()
  print("Árvore Trie de Palavras\n")
  print("1 - Adicionar Palavra")
  print("2 - Pesquisar Palavra")
  print("3 - Remover Palavra\n")
  print("Escolha uma opção: ",end='')
  escolha = int(input())

  if escolha == 1:
    replit.clear()
    print("Palavra a ser adicionada: ",end='')
    dicionario.adicionar(input())
    time.sleep(2)
    menu()

  if escolha == 2:
    replit.clear()
    print("Palavra a ser pesquisada: ",end='')
    dicionario.pesquisar(input())
    time.sleep(2)
    menu()

  if escolha == 3:
    replit.clear()
    print("Palavra a ser removida: ",end='')
    dicionario.remover(input())
    time.sleep(2)
    menu()

dicionario = Trie()
menu()
