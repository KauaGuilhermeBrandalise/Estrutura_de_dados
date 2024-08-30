class VetorNaoOrdenado:
    def __init__(self):
        self.vetor = []

    def inserir(self, elemento):
        self.vetor.append(elemento)

    def imprimir(self):
        print("Vetor atual:", self.vetor)

    def pesquisar(self, elemento):
        if elemento in self.vetor:
            print(f"Elemento '{elemento}' encontrado no vetor.")
        else:
            print(f"Elemento '{elemento}' não encontrado no vetor.")

    def excluir(self, posicao):
        if 0 <= posicao < len(self.vetor):
            removido = self.vetor.pop(posicao)
            print(f"Elemento '{removido}' removido da posição {posicao}.")
        else:
            print("Posição inválida.")

meu_nome = input('Digite seu nome: ')

vetor = VetorNaoOrdenado()

print("Inserindo os caracteres do nome...")
for char in meu_nome:
    vetor.inserir(char)
    vetor.imprimir()  

print("\nVetor final após todas as inserções:")
vetor.imprimir()

print("\nPesquisando por caracteres no vetor:")
vetor.pesquisar('k')
vetor.pesquisar('a')
vetor.pesquisar('u')

print("\nExclusões de elementos no início, meio e fim:")
vetor.excluir(0)  
vetor.imprimir()

meio = len(vetor.vetor) // 2  
vetor.excluir(meio)
vetor.imprimir()

vetor.excluir(len(vetor.vetor) - 1)  
vetor.imprimir()

print("\nVetor após as exclusões:")
vetor.imprimir()
