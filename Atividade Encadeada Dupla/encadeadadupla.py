class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

class EncadeadaDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.Nulo = None

    def lista_vazia(self):
        return self.primeiro == self.Nulo

    def insere_inicio(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
            novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        if self.lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        self.ultimo = novo
        
    def excluir_inicio(self):
        if self.lista_vazia():
            return None
        temp = self.primeiro
        if self.primeiro.proximo == self.Nulo:  # Se houver apenas um elemento
            self.ultimo = self.Nulo
        else:
            self.primeiro.proximo.anterior = self.Nulo
        self.primeiro = self.primeiro.proximo
        return temp
    
    def excluir_final(self):
        if self.lista_vazia():
            return None
        temp = self.ultimo
        if self.primeiro.proximo == self.Nulo:  # Se houver apenas um elemento
            self.primeiro = self.Nulo
        else:
            self.ultimo.anterior.proximo = self.Nulo
        self.ultimo = self.ultimo.anterior
        return temp

    def excluir_qualquer(self, valor):
        atual = self.primeiro
        while atual != self.Nulo and atual.valor != valor:
            atual = atual.proximo
        if atual == self.Nulo:
            return None
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo
        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
        return atual

    def mostrar_inicio(self):
        atual = self.primeiro
        while atual != self.Nulo:
            print(atual.valor, end=" ")
            atual = atual.proximo
        print()

    def mostrar_final(self):
        atual = self.ultimo
        while atual != self.Nulo:
            print(atual.valor, end=" ")
            atual = atual.anterior
        print()

    def pesquisar(self, valor):
        if self.lista_vazia():
            print("Erro: lista vazia.")
            return None
        atual = self.primeiro
        while atual != self.Nulo and atual.valor != valor:
            atual = atual.proximo
        if atual == self.Nulo:
            return None
        return atual

# Demonstração das operações com o nome "Kauã"

lista = EncadeadaDupla()

# a. Inserir cada caractere do nome "Kauã"
nome = "Kauã"
for char in nome:
    lista.insere_final(char)

# b. Mostrar todos os elementos
print("Elementos na lista (do início):")
lista.mostrar_inicio()

# c. Excluir o primeiro elemento
lista.excluir_inicio()

# d. Verificar se a exclusão foi concluída
print("Elementos na lista após excluir o primeiro:")
lista.mostrar_inicio()

# e. Pesquisar o último caractere "ã"
resultado = lista.pesquisar('ã')
if resultado:
    print(f"O caractere 'ã' foi encontrado: {resultado.valor}")
else:
    print("Caractere 'ã' não foi encontrado")

# f. Excluir um elemento qualquer (nesse caso, o 'u')
lista.excluir_qualquer('u')

# g. Verificar se a exclusão foi concluída
print("Elementos na lista após excluir 'u':")
lista.mostrar_inicio()
