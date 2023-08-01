import random
def tCraps(n):
    x = 0
    while x < n:
        dado_1 = random.randrange(1,7)
        dado_2 = random.randrange(1,7)
        venceu = 0
        perdeu = 0
        result = dado_1 + dado_2
        if result == 7 or result == 11:
            venceu += 1
        x += 1
    return print(f'{(venceu/n):6.4f}') 