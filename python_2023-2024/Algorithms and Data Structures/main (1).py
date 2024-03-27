def fib(n):
    if n<0:
        return None
    elif n<2:
        return n
    lista = [0, 1] + [0] * (n-1)
    print(lista)

    for i in range(2, n+1):
        lista[i] = lista[i-1] + lista[i-2]
    print(lista)
    return lista[n]

print(fib(19))