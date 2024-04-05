def secantes(f, x0, x1, tol, max_iter):
    iter_count = 0
    print("k\t\t\t a\t\t\t\t b\t\t\t\t c\t\t\t\t tol")
    while abs(f(x1)) > tol and iter_count < max_iter:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        iter_count += 1
        print ('%s:\t\t\t %s\t\t\t %s\t\t\t %s\t\t\t%f'% (iter_count,x0,x1,x2,abs(f(x1))))
    return x1

def f(x):
    return (980/x) * (1- 2.718281**(-x/100))-5

x0 = 100
x1 = 200
tolerancia = 1e-6
max_iteracoes = 100

resultado = secantes(f, x0, x1, tolerancia, max_iteracoes)
print("O resultado aproximado da equação é:", resultado)
