def muitos(namefile):
    file = open(namefile, 'r')
    cont = file.read()
    file.close()
    lst = cont.split()
    acum_1 = 0
    acum_2 = 0
    acum_3 = 0
    acum_4 = 0
    for i in lst:
        if len(i) == 1:
            acum_1 += 1
        elif len(i) == 2:
            acum_2 += 1
        elif len(i) == 3:
            acum_3 += 1
        elif len(i) == 4:
            acum_4 += 1
        else:
            pass
    print(f'Palavras de tamanho 1: {acum_1}.')
    print(f'Palavras de tamanho 2: {acum_2}.')
    print(f'Palavras de tamanho 3: {acum_3}.')
    print(f'Palavras de tamanho 4: {acum_4}.')