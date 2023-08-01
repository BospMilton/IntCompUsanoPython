import random

def simul(n):
    cont_jg1 = 0
    cont_jg2 = 0
    x = 0
    while x < n:
        jg1 = random.randrange(0,2)
        jg2 = random.randrange(0,2)
        if jg1 == jg2:
            pass
        elif jg1 == 0 and jg2 == 2 or jg1 == 2 and jg2 == 1 or jg1 == 1 and jg2 == 0:
                cont_jg1 += 1
        elif jg2 == 0 and jg1 == 2 or jg2 == 2 and jg1 == 1 or jg2 == 1 and jg1 == 0:
            cont_jg2 += 1        
        x += 1
    if cont_jg1 == cont_jg2:
        print('Empate')
    elif cont_jg1 > cont_jg2:
        print('Jogador 1 ganhou.')
    else:
        print('Jogador 2 ganhou.')