def geo(lst):
    for i in range(len(lst)):
            if lst[i]/lst[i-1] == c:
                cont += 1
    if cont == len(lst)-1:
        print(True)
    else:
        print(False)