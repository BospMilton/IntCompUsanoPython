def ion2e(nome):
    if nome[-3] == 'i' and nome[-2] == 'o' and nome[-1] == 'n':
       return print(nome[0:len(nome)-3], end='e')
    else:
        return print(nome)