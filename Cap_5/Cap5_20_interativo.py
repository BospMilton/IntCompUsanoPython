def inter(lst1,lst2):
    lst_res = []
    for i in lst1:
        for j in lst2:
            if i == j:
                lst_res.append(i)
    print(lst_res)
