class Pilha:
    def __init__(self, capacidade):
        self.topo = -1
        self.capacidade = capacidade
        self.valores = [None] * capacidade
    
    def empilhar(self, valor):
        if self.pilhaCheia():
            print("Pilha cheia! Não é possível empilhar.")
        else:
            self.topo = self.topo +1
            self.valores[self.topo] = valor
            print(f"Empilhado: {valor}")
    
    def desempilhar(self):
        if self.pilhaVazia():
            print("Pilha vazia! Não é possível desempilhar.")
        else:
            valor_removido = self.valores[self.topo]
            self.topo = self.topo -1 
            print(f"Desempilhado {valor_removido}")           
    
    def pilhaVazia(self):
        return self.topo == -1
    
    def pilhaCheia(self):
        return self.topo == self.capacidade -1
    
    def verTopo(self):
        if not self.pilhaVazia():
            return self.valores[self.topo]
        else:
            return None
        
    
pilha = Pilha(4)

nome = "Kauã"
for char in nome:
    pilha.empilhar(char)

print("\nPilha cheia?", pilha.pilhaCheia())

print("Elemento no topo da pilha:", pilha.verTopo())

for _ in range(3):
    pilha.desempilhar()

print("Elemento no topo da pilha após 3 desempilhamentos:", pilha.verTopo())
