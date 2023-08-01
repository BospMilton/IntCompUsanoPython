def poli(lst,x):
    fat = 0
    n = 0
    while n < len(lst):
        for i in lst:
            fat = fat + i*x**n
            n += 1 
    return fat
