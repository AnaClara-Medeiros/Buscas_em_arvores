# -*- coding: utf-8 -*-

class TreeNode: #árvore para os nós
  def __init__(self, x): 
      self.valor = x #x = chave que vou inserir no nó
      self.esquerda = None #filho da esquerda
      self.direita = None #filho da direita

def valor_proximo(arvore, valor): #árvore e valor que ele vai procurar
    valor_raiz = arvore.valor
    if valor < valor_raiz: #se for, vou para esquerda
        node = arvore.esquerda
    else: #vai para a direita
        node = arvore.direita
    if not node: #se não tiver filhos
        return valor_raiz #retorna a raiz

    proximo = valor_proximo(node, valor) #chamo ela de novo e vejo o filho que eu achei
    #se for da direita ou esquerda, ele vai procurar o valor novamente

    '''Tenho dois valores, o último valor_proximo e a última raiz'''
  
    return min((valor_raiz, proximo), key = lambda x: abs(valor - x))

  #passo o valor x como as variáveis que quero comparar (raiz, valor)
  #subtraio ele do valor que procuro pra ver qual ter a menor diferenã (mínimo)
  #abs: módulo, retorna só número positivo. Pq pode ser 23 - 24, mas a diferença ainda é 1 positivo

if __name__ == '__main__': #quando puxar esse arqv não vai chamar o que está a seguir
  tree = TreeNode(8) #criando a árvore
  tree.esquerda = TreeNode(5) #filho da esquerda
  tree.direita = TreeNode(14) #filho da direita
  tree.esquerda.equerda = TreeNode(4) #filho da esquerda do filho da esquerda
  tree.esquerda.direita = TreeNode(6) #filho da direita do filho da esquerda
  tree.esquerda.direita.esquerda = TreeNode(3)
  tree.esquerda.direita.direita = TreeNode(7)
  tree.direita.direita = TreeNode(24)
  tree.direita.direita.esquerda = TreeNode(22)

  resultado = valor_proximo(tree, 23)
  print(resultado)
