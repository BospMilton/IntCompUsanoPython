def fib(n):
    ultimo=1
    penultimo=1
    if (n==1) or (n==2):
        return print("1")
    else:
        count=3
        while count <= n:
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            count += 1
        return termo