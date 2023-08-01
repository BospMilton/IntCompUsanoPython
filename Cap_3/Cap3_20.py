lst = [2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(lst)):
    if (lst[i]**2%8) == 0:
        print(lst[i])