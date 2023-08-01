x = 0
lst = []
soma = 0

while x < 4:
    num = eval(input(f'Digite o {x+1}º número: '))
    x += 1
    lst.append(num)

x = 0 
while x < 3:
    soma += lst[x]
    x += 1
if soma/3 == lst[3]:
    print('Igual.')
else: 
    print('Não é igual.')