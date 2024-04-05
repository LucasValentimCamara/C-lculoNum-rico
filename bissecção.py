def bissecao(f, a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        raise ValueError("A função deve ter sinais opostos em a e b.")
    
    iter_count = 0
    print("k\t a\t\t\t\t b\t\t\t\t c\t\t\t\t tol")
    while abs(b - a) > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0: return c
        if f(a) * f(c) < 0: b = c
        else: a = c
        iter_count += 1
        print ('%s:\t %s\t\t\t %s\t\t\t %s\t\t\t%f'% (iter_count,a,b,c,abs(b - a)))
    return (a + b) / 2

def f(x):
    return (980/x) * (1- 2.718281**(-x/100))-5

a = 100
b = 200
tolerancia = 1e-6
max_iteracoes = 1000

resultado = bissecao(f, a, b, tolerancia, max_iteracoes)
print("O resultado aproximado da equação é: x =", resultado)