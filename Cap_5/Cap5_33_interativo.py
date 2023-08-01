def mist(n):
    cont = 0
    for i in range(n):
        if n//2 >= 1:
            cont += 1
        n = n//2
    return cont
