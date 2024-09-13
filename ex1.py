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
    print("Vetor", vetor)

def pesquisa_caractere(vetor, caractere):
    if caractere in vetor:
        print(f"O caracter {caractere} esta presente no vetor.")
    else:
        print(f"O caracter {caractere} não esta presente no vetor.")

def remover_vetor(vetor, valor):
    if valor in vetor:
        vetor.remove(valor)
        print(f"O caractere {valor} foi removido do vetor.")                     
    else:
        print(f"O caractere {valor} não foi encontrado no vetor.")

vetor = [] 

nome = "Kauã"
for char in nome:
    vetorordenado(vetor, char)

imprimir_vetor(vetor)

pesquisa_caractere(vetor, "K")
pesquisa_caractere(vetor, "u")
pesquisa_caractere(vetor, "l")

if vetor:
    remover_vetor(vetor, vetor[0])

if vetor:
    meio = len(vetor)//2
    remover_vetor(vetor, vetor[meio])

if vetor:
    remover_vetor(vetor, vetor[-1])

imprimir_vetor(vetor)