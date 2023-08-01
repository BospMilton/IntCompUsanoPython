def amb(lst_1, lst_2):
    acum = 0
    for i in lst_1:
        for j in lst_2:
            if i == j:
                acum += 1
    if acum > 0:
        print(True)
    else:
        print(False)