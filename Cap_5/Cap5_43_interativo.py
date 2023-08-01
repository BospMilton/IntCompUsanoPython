def lpar(lst):
    cont = 0
    for i in range(len(lst)):
        if sum(lst[i])%2 == 0:
            cont += 1
    if cont == len(lst):
        print(True)
    else:
        print(False)