def dup(file):
    file1 = open(file, 'r')
    cont = file1.read()
    file1.close()
    lst = cont.split()

    cont1 = 0
    cont2 = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                cont1 += 1
            else: 
                cont2 += 1
    if cont1 > 0:
        print(True)