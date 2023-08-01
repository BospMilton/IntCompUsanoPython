def trad(dsc):
    while True:
        word = input('Digite uma frase: ')
        if word == '':
            break
        n_word = word.split()
        for i in n_word:
            if i in dsc:
                print(f'{dsc[i]}', end=' ')
            else:
                print('----',end=' ')
        print()
