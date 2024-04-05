import numpy as np

def sor(A, b, w, tol=1e-5, max_iter=1000):
    n = len(A)
    x = np.zeros(n)
    x_ant = np.zeros(n)
    iter_count = 0

    while np.linalg.norm(x - x_ant) > tol and iter_count < max_iter:
        x_ant = x.copy()
        for i in range(n):
            x[i] = (1 - w) * x[i] + (w / A[i, i]) * (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x_ant[i + 1:]))

        iter_count += 1

    return x, iter_count

# Exemplo de sistema linear (matriz A e vetor b)
A = np.array([[4, -1, 0, 0],
              [-1, 4, -1, 0],
              [0, -1, 4, -1],
              [0, 0, -1, 3]], dtype=float)

b = np.array([5, 5, 10, 15], dtype=float)

# Encontrando o melhor valor de w e a quantidade de iterações para cada valor de w
print("w | Número de Iterações")
print("-" * 23)

best_w = None
min_iterations = float('inf')

for w in np.linspace(0, 2, num=21):
    _, iterations = sor(A, b, w)
    print(f"{w:.1f} | {iterations}")

    if iterations < min_iterations:
        min_iterations = iterations
        best_w = w

# Resolvendo o sistema usando o melhor valor de w
solucao, _ = sor(A, b, best_w)

# Exibindo o vetor solução
print("\nVetor solução:")
print(solucao)
