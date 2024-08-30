

def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 ==0:
            pares.append(numero)
    return pares

lista_inteiros = [1, 3, 5, 6, 8, 12, 2, 4]
resultado = filtrar_pares(lista_inteiros)
print(resultado)