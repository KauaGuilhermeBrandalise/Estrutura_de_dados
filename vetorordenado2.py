def print_vector(v):
    print(v)

def insert_element(vector, element):
    # Encontra a posição correta para inserir o novo elemento
    i = 0
    while i < len(vector) and vector[i] is not None and vector[i] < element:
        i += 1
    
    # Realoca os elementos à direita da posição de inserção
    if i < len(vector):
        for j in range(len(vector) - 1, i, -1):
            vector[j] = vector[j - 1]
        vector[i] = element
    else:
        raise IndexError("O vetor está cheio e não pode inserir novos elementos.")

def linear_search(vector, target):
    for i in range(len(vector)):
        if vector[i] == target:
            return i
    return -1

def binary_search(vector, target):
    left, right = 0, len(vector) - 1
    while left <= right:
        # Ignora posições com None
        while left <= right and vector[left] is None:
            left += 1
        while left <= right and vector[right] is None:
            right -= 1
        if left > right:
            break
        
        mid = (left + right) // 2
        if vector[mid] == target:
            return mid
        elif vector[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


vector_capacity = 7
vector = [2, 3, 5, 7] + [None] * (vector_capacity - 4)

ultima_posicao = len([x for x in vector if x is not None]) - 1
print(f"a. Valor de ultima_posicao: {ultima_posicao}")

element_to_insert = 4
insert_element(vector, element_to_insert)
print("b. Vetor após inserção do elemento 4:")
print_vector(vector)

num_iterations = len([x for x in vector if x is not None]) - 1 - 1
print(f"Num iterações para realocar elementos: {num_iterations}")

ultima_posicao = len([x for x in vector if x is not None]) - 1
print(f"c. Novo valor de ultima_posicao: {ultima_posicao}")

target_value = 7
linear_index = linear_search(vector, target_value)
print(f"d. Índice do valor {target_value} com pesquisa linear: {linear_index}")

binary_index = binary_search(vector, target_value)
print(f"e. Índice do valor {target_value} com pesquisa binária: {binary_index}")
