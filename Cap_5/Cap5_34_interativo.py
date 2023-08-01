def ext(lst):
    dep = 0
    ret = 0
    lst_c = []
    for i in range(len(lst)):
        if lst[i] > 0:
            dep = dep + lst[i]
        else: 
            ret = ret + lst[i]
    print(dep)
    print(ret)