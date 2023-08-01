def ssoma(lst,alv):
    cont = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            for k in range(len(lst)):
                if lst[i]+lst[j]+lst[k] == alv:
                    cont += 1
    if cont > 0:
        return True
    else: 
        return False
                            