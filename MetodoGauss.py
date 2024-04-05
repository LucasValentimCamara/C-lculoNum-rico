import numpy as np

def pivotamento_parcial(A, b):
    n = len(A)
    num_iteracoes = 0  # Inicializando o contador de iterações

    for i in range(n):
        pivot = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[pivot][i]):
                pivot = k
        if pivot != i:
            num_iteracoes += 1  # Incrementando o contador de iterações
            A[i], A[pivot] = A[pivot], A[i].copy()
            b[i], b[pivot] = b[pivot], b[i]

    return A, b, num_iteracoes

def gauss_pivoteamento_parcial(A, b):
    n = len(A)
    A, b, num_iteracoes_pivot = pivotamento_parcial(A, b)  # Obtendo o número de iterações do pivoteamento

    for i in range(n):
        for j in range(i + 1, n):
            fator = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= fator * A[i][k]
            b[j] -= fator * b[i]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]

    return x, num_iteracoes_pivot

# Exemplo de sistema linear (matriz A e vetor b)
A = np.array([[10, 0, 0, 5 ,8, 0, 2, 0, 0],
              [-1, -1, 0, 0, 1, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 1, 0, 0, 0],
              [1, 0, 0, -1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, -1, 0, 1, -1, 0],
              [0, 0, 0, 0, 0, -1, 0, 1, 1],
              [0, 0, 0, 1, 0, 0, -1, 0, 0],
              [0, -5, 0, 0, -8, 5, 0, 10, 0],
              [0, 0, 2, 0, 0, -5, 0, 0, -8]], dtype=float)

b = np.array([0, 0, 0, 0, 0, 0, 0, 0, 95], dtype=float)

# Resolvendo o sistema usando Gauss com pivoteamento parcial
solucao, num_iteracoes_pivot = gauss_pivoteamento_parcial(A.tolist(), b.tolist())

# Exibindo as etapas intermediárias
print("Matriz aumentada:")
print(np.column_stack((A, b)))

# Escalonamento
for i in range(len(solucao)):
    for j in range(i + 1, len(solucao)):
        A[j][i] = 0

print("\nMatriz escalonada aumentada:")
print(np.column_stack((A, b)))

# Exibindo o sistema triangular superior
print("\nSistema triangular superior:")
for i in range(len(A)):
    print(A[i])

# Exibindo o vetor solução
print("\nVetor solução:")
print(solucao)

# Exibindo o número de iterações de pivoteamento realizadas
print("\nNúmero de iterações de pivoteamento:", num_iteracoes_pivot)
