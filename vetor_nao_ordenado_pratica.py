import numpy as np

class VetorNaoOrdenado:
 def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = [''] * capacidade

 def inserir(self, valor):
    if self.ultima_posicao == self.capacidade - 1:
        print('Vetor cheio!!! Valor {} não inserido'.format(valor))
    else:
        self.ultima_posicao += 1
        self.valores[self.ultima_posicao] = valor

 def imprimir(self):
    if self.ultima_posicao == -1:
        print("Vetor vazio!!!")
    else:
        print("Imprimindo array...")
    for i in range(self.ultima_posicao + 1):
        print('Posição {} | Valor {}'.format(i, self.valores[i]))
def pesquisar(self, valor):
 for i in range(self.ultima_posicao + 1):
    if (valor == self.valores[i]):
        return i
    return -1

 def excluir(self, valor):
    pos = self.pesquisar(valor)
    if (pos == -1):
        return -1
    else:
        for i in range(pos, self.ultima_posicao):
            self.valores[i] = self.valores[i+1]
            self.ultima_posicao = self.ultima_posicao - 1

 def inserir_sem_duplicata(self, valor):
    if self.ultima_posicao == self.capacidade - 1:
        print('Vetor cheio!!! Valor {} não inserido'.format(valor))
    elif self.pesquisar(valor) != -1: print('Valor já existe!!! Valor {} não inserido'.format(valor))
    else:
        self.ultima_posicao += 1
        self.valores[self.ultima_posicao] = valor

vetor = VetorNaoOrdenado(10)
vetor.imprimir()
vetor.inserir(4)
vetor.inserir_sem_duplicata(4)
vetor.inserir(3)
# 15/08/2024, 16:02 Aula 03 - Pratica - Vetores não ordenados - Estrutura de Dados - UNISATC.py
# localhost:62348/ 1/2
vetor.inserir(1)
vetor.inserir(5)
vetor.inserir(6)
vetor.inserir(9)
vetor.inserir(2)
vetor.inserir(8)
vetor.inserir(0)
vetor.inserir(7)

vetor.inserir(7) #vai estourar o limite do array

vetor.imprimir()

posicao = vetor.pesquisar(0)
print("A posicao do zero é {}".format(posicao))

vetor.excluir(0)
vetor.imprimir()