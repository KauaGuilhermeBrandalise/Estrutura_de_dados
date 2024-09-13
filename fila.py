class Fila:
    def __init__(self, capacidade):
        self.inicio = 0
        self.final = -1
        self.elementos = 0
        self.capacidade = capacidade
        self.valores = [None] * capacidade
    
    def enfileirar(self,valor):
        if self.filaCheia():
            print("Fila cheia! Não é possível enfileirar.")
            return
        if self.final == self.capacidade - 1:
            self.final = - 1
        self.final = self.final + 1
        self.valores[self.final] = valor
        self.elementos = self.elementos + 1
        print(f"Enfileirando {valor}.")
        self.mostrarFila()
    
    def desenfileirar(self):
        if self.filaVazia():
            print("Fila vazia! Não é possível desenfileirar.")
            return None
        temp = self.valores[self.inicio]
        self.inicio = self.inicio + 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.elementos = self.elementos - 1
        # print(f"Desenfileirando {temp}")
        self.mostrarFila()
        return temp
    
    def filaVazia(self):
        return self.elementos == 0
    
    def filaCheia(self):
        return self.elementos == self.capacidade
    
    def primeiroElemento(self):
        if self.filaVazia():
            return - 1
        return self.valores[self.inicio]

    def mostrarFila(self):
        # Mostra os elementos da fila
        print("Fila atual:", [self.valores[(self.inicio + i) % self.capacidade] for i in range(self.elementos)])

fila = Fila(4)

nome = "Kauã"
for char in nome:
    fila.enfileirar(char)

print("\nFila cheia?", fila.filaCheia())

print("Primeiro elemento da fila:", fila.primeiroElemento())

for _ in range(3):
    fila.desenfileirar()

print("Primeiro elemento da fila após 3 desenfileiramentos:", fila.primeiroElemento())
