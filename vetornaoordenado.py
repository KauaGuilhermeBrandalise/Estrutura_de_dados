class Vetornaoordenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaposicao = -1
        self.valores = [''] * capacidade

    def inserir(self, valor):
        if self.ultimaposicao == self.capacidade -1:
            print("Vetor cheio")
        else:
            self.ultimaposicao += 1
            self.valores[self.ultimaposicao] = valor

    def imprimir(self):
        if self.ultimaposicao == -1:
            print("Vetor vazio")
        else:
            for i in range(self.ultimaposicao + 1):
                print("Posição {} | Valor {}"
                      .format(i,self.valores[i]))
    def pesquisar(self, valor):
        for i in range(self.ultimaposicao + 1):
            if self.valores[i] == valor:
                return i
            return -1
    
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return-1
        else:
            for i in range(posicao, self.ultimaposicao):
                self.valores[i] = self.valores[i+1]
            self.ultimaposicao -= 1
            

meuvetor = Vetornaoordenado(4)
meuvetor.imprimir() 
meuvetor.inserir(2) 
meuvetor.inserir(17) 
meuvetor.inserir(7) 
meuvetor.inserir(25)
meuvetor.inserir(66)
meuvetor.imprimir()

print(meuvetor.pesquisar(17))
print(meuvetor.pesquisar(35))
print(meuvetor.pesquisar(25))
meuvetor.excluir(17)
meuvetor.imprimir()
print(meuvetor.excluir(55))