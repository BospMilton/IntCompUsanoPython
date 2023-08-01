lst = []

x = 0
while x < 3: 
    lst.append(input('Digite uma palavra: '))
    x += 1
if lst[0]<lst[1] and lst[1]<lst[2]:
    print(True)