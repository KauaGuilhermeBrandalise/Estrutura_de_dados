
def vetorordenado(vetor, valor):
    if not vetor:
        vetor.append(valor)
    else:
        inserido = False
        for i in range(len(vetor)):
            if valor < vetor[i]:
                vetor.insert(i, valor)
                inserido = True
                break
        if not inserido:
            vetor.append(valor)

def imprimir_vetor(vetor):
    print("Vetor:", vetor)

def pesquisar_caractere(vetor, caractere):
    if caractere in vetor:
        print(f'O caractere "{caractere}" está presente no vetor.')
    else:
        print(f'O caractere "{caractere}" não está presente no vetor.')

def remover_vetor(vetor, valor):
    if valor in vetor:
        vetor.remove(valor)
        print(f'O caractere "{valor}" foi removido do vetor.')
    else:
        print(f'O caractere "{valor}" não foi encontrado no vetor.')

vetor = []

nome = "Kauã"
for char in nome:
    vetorordenado(vetor, char)

imprimir_vetor(vetor)

pesquisar_caractere(vetor, 'a')
pesquisar_caractere(vetor, 'u')
pesquisar_caractere(vetor, 'm')

# d. Exclusão de caracteres do início, meio e final
# Remove do início (primeiro caractere)
if vetor:
    remover_vetor(vetor, vetor[0])

# Remove do meio (caractere central, se houver)
if vetor:
    meio = len(vetor) // 2
    remover_vetor(vetor, vetor[meio])

# Remove do final (último caractere)
if vetor:
    remover_vetor(vetor, vetor[-1])

# e. Impressão do vetor após as remoções
imprimir_vetor(vetor)
