import random
def moeda():
    moeda = random.randrange(0,2)
    if moeda == 1:
        print('Cara')
    else: 
        print('Coroa')