def conta_str(palavra):
    contagem = {}
    for caractere in palavra:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    return contagem

texto = "laranja"
resultado = conta_str(texto)
print (resultado)