num = int(input('Digite um número: '))

x = 1
while x <= num:
    if num%x == 0:
        print(f'{x}')
    x += 1