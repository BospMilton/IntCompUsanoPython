lst = []

t_lst = eval(input('Digite o tamanho da lista: '))

x = 0
while x < t_lst:
    lst.append(input('Digite um número para a lista: '))
    x += 1
    print()

print(f'O primeiro número da lista é {lst[0]}.')
print()
print(f'E o último número da lista é {lst[-1]}')
print()
