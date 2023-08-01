import random

def craps():
    dado_1 = random.randrange(1,7)
    dado_2 = random.randrange(1,7)
    result = dado_1 + dado_2
    if result == 7 or result == 11:
        print('O jogador venceu.')
    elif result == 2 or result == 3 or result == 12:
        print('O jogador perdeu.')




