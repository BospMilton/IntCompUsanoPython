def name():
    dsc = {}
    while True:
        name = input('Digite um nome: ')
        if name == '':
            break
        else:
            if name in dsc:
                dsc[name] += 1
            else:
                dsc[name] = 1
    for name in dsc:
        print('Há {} alunos chamados de {}.'.format(dsc[name],name))    