def fprimo(n):
    lst = []
    div = 2
    while n > 1:
        while n % div == 0:
            lst.append(div)
            n //= div
        div += 1
    return lst