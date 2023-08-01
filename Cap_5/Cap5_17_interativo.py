def db(lst):
    for i in range(len(lst)):
        if lst[i] == 2*lst[i-1]:
            return print(lst[i])
    