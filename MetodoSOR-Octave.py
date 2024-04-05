import numpy as np

def Sor(A, b, n, x0, omega):
    Nmax = 10000
    iter = 1
    tol = 0.0000001
    xat = x0.copy()

    while iter < Nmax:
        xnew = np.zeros(n)
        for i in range(n):
            somaimenor = 0.0
            somaimaior = 0.0

            for j in range(n):
                if j < i:
                    somaimenor += A[i, j] * xat[j]
                if j > i:
                    somaimaior += A[i, j] * xat[j]

            xnew[i] = (1.0 - omega) * xat[i] + omega * (-somaimenor - somaimaior + b[i]) / A[i, i]
            xat[i] = xnew[i]

        c = np.abs(xnew - x0)
        maximo = np.max(c)

        if maximo < tol:
            print(f"Convergiu com {iter} iteracoes")
            break
        else:
            iter += 1
            x0 = xnew.copy()

    return xnew

def funcaoSor():
    np.set_printoptions(precision=15, suppress=True)
    
    # Matriz A
    A = np.array([[10, 0, 0, 5, 8, 0, 2, 0, 0],
                  [-1, -1, 0, 0, 1, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0, 1, 0, 0, 0],
                  [1, 0, 0, -1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, -1, 0, 1, -1, 0],
                  [0, 0, 0, 0, 0, -1, 0, 1, 1],
                  [0, 0, 0, 1, 0, 0, -1, 0, 0],
                  [0, -5, 0, 0, -8, 5, 0, 10, 0],
                  [0, 0, 2, 0, 0, -5, 0, 0, -8]])

    n = 9

    # Vetor b
    b = np.array([0, 0, 0, 0, 0, 0, 0, 0, 95])

    # X inicial
    x0 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])

    # Relaxação omega
    omega = 1

    print('Método Sor ')
    print('\n Matriz A = ')
    print(A)
    x = Sor(A, b, n, x0, omega)
    print('Resolvendo o sistema Ax=b')
    print('Solução: x=')
    print(x)
    print('Verificando...')
    print('Ax=    ')
    resp = A.dot(x)
    print(resp)

funcaoSor()
