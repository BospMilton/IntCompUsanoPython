import math #para irmos nos familiarizando

x = eval(input('Digite a coordenada X: '))
y = eval(input('Digite a coordenada Y: '))
print()
r_0 = math.sqrt(math.pow(x,2)+math.pow(y,2))

if r_0 <= 8:
    print('Esta dentro!')
    print()