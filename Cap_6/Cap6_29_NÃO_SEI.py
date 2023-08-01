npeople = 5
lst = [(0,1),(1,2),(3,4)]

for amigo in lst:
    for i in amigo:
        if i in amigo:
            print('ok')

print(len(lst))