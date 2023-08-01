def pix(lst):
    cont = 0
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] > 0:
                cont += 1
    return cont