def avg(lst):
    lst2 = []
    soma = []
    for i in lst:
        lst2.append(sum(i))
        soma.append(len(i))
    for i in range(len(lst2)):
        print(f'{lst2[i]/soma[i]}')

