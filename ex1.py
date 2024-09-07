class Fila:
    def __init__(self, capacidade):
        self.inicio = 0
        self.final = -1
        self.elementos = 0
        self.capacidade = capacidade
        self.valores = [''] * capacidade

    def fila_vazia(self):
        return self.elementos == 0

    def fila_cheia(self):
        return self.elementos == self.capacidade

    def enfileirar(self, valor):
        if self.fila_cheia():
            print("Erro: Fila cheia.")
            return
        self.final = (self.final + 1) % self.capacidade
        self.valores[self.final] = valor
        self.elementos += 1
        print(f"Enfileirado: {valor}")

    def desenfileirar(self):
        if self.fila_vazia():
            print("Erro: Fila vazia.")
            return None
        temp = self.valores[self.inicio]
        self.inicio = (self.inicio + 1) % self.capacidade
        self.elementos -= 1
        print(f"Desenfileirado: {temp}")
        return temp

    def primeiro_elemento(self):
        if self.fila_vazia():
            print("A fila está vazia.")
            return None
        return self.valores[self.inicio]

    def imprimir_fila(self):
        if self.fila_vazia():
            print("A fila está vazia.")
        else:
            fila = []
            i = self.inicio
            for _ in range(self.elementos):
                fila.append(self.valores[i])
                i = (i + 1) % self.capacidade
            print("Fila:", fila)


# Nome: Kauã (4 caracteres, capacidade da fila será 4)
nome = "Kauã"
fila = Fila(len(nome))

# a. Teste o método “filaVazia()” através do método “desenfileirar()”
print("Testando filaVazia:")
fila.desenfileirar()

# b. Demonstrar o enfileiramento de cada um dos caracteres que compõem o nome
print("\nEnfileirando os caracteres do nome:")
for char in nome:
    fila.enfileirar(char)

fila.imprimir_fila()

# c. Teste o método “filaCheia()” através do método “enfileirar(valor)”
print("\nTestando filaCheia:")
fila.enfileirar('X')  # Tentativa de enfileirar após a fila estar cheia

# d. Demonstrar qual elemento é o primeiro da fila
print("\nPrimeiro elemento da fila:")
primeiro = fila.primeiro_elemento()
if primeiro:
    print(f"O primeiro elemento é: {primeiro}")

# e. Execute o método “desenfileirar()” por três vezes e verifique qual elemento é o primeiro da fila
print("\nDesenfileirando três elementos:")
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()

print("\nPrimeiro elemento após três desenfileiramentos:")
primeiro = fila.primeiro_elemento()
if primeiro:
    print(f"O primeiro elemento é: {primeiro}")

fila.imprimir_fila()
