class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.vetor = [None] * capacidade  
        self.ultima_posicao = -1 
    
    def inserir(self, elemento):
        if self.ultima_posicao < len(self.vetor) - 1:  # Verifica se há espaço no vetor
            self.ultima_posicao += 1
            self.vetor[self.ultima_posicao] = elemento
        else:
            print("Vetor cheio.")
    
    def imprimir(self):
        if self.ultima_posicao == -1:
            print("Vetor vazio.")
        else:
            print("Vetor:", self.vetor[:self.ultima_posicao + 1])
    
    def excluir(self, indice):
        if indice < 0 or indice > self.ultima_posicao:
            print("Índice inválido.")
            return
        
        for i in range(indice, self.ultima_posicao):
            self.vetor[i] = self.vetor[i + 1]
        
        self.vetor[self.ultima_posicao] = None
        self.ultima_posicao -= 1

vetor = VetorNaoOrdenado(7)

vetor.inserir('S')
vetor.inserir('A')
vetor.inserir('T')
vetor.inserir('C')

print(f"Ultima posição antes da exclusão: {vetor.ultima_posicao}")
vetor.imprimir()

print("\nExcluindo o elemento de índice 1 ('A') e realocando os demais...")
vetor.excluir(1)

print("\nVetor após a exclusão:")
vetor.imprimir()


print(f"Nova ultima_posicao após exclusão: {vetor.ultima_posicao}")


def pesquisar(vetor, elemento):
    encontrado = False
    for i in range(vetor.ultima_posicao + 1):
        if vetor.vetor[i] == elemento:
            encontrado = True
            break
    return encontrado

elemento_a_pesquisar = 'T'
if pesquisar(vetor, elemento_a_pesquisar):
    print(f"\nElemento '{elemento_a_pesquisar}' encontrado no vetor.")
else:
    print(f"\nElemento '{elemento_a_pesquisar}' não encontrado no vetor.")
