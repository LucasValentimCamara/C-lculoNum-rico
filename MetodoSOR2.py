# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 23:01:53 2023

@author: lucas
"""

import numpy as np
import pandas as pd

def sor_solver(A, b, w, max_iter=1000, tol=1e-5):
    n = len(A)
    x = np.zeros(n)
    for _ in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (1 - w) * x[i] + (w / A[i, i]) * (b[i] - s1 - s2)
        if np.linalg.norm(x_new - x, np.inf) < tol:
            break
        x = x_new
    return x

def main():
    # Solicitar a entrada da matriz 9x9
    print("Digite os elementos da matriz 9x9 (separados por espaço e linha por linha):")
    A = np.zeros((9, 9))
    for i in range(9):
        A[i] = input().split()
    
    # Convertendo a entrada para valores numéricos
    A = A.astype(float)

    # Solicitar a entrada do array de 9 itens
    print("Digite os 9 elementos do vetor (separados por espaço):")
    b = np.array(input().split(), dtype=float)

    w_values = np.linspace(0, 2, 21)  # Valores de w entre 0 e 2 com incremento de 0.1
    iterations = []

    for w in w_values:
        x = sor_solver(A, b, w)
        iterations.append(len(x))

    data = {'w': w_values, 'Iterações': iterations}
    df = pd.DataFrame(data)
    print(df)

    best_w = w_values[np.argmin(iterations)]
    best_solution = sor_solver(A, b, best_w)
    print("\nMelhor escolha de w:", best_w)
    print("Vetor solução (x):", best_solution)

if __name__ == "__main__":
    main()
