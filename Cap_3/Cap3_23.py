lst = ['Ellie', 'Steve', 'Sam', 'Owen', 'Gavin']

x = 0
for i in lst:
    if lst[x][0] > 'A' and lst[x][0] < 'M':
        print(lst[x])
    x += 1