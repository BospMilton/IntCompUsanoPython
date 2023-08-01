def media():
    stç = input('Digite uma sentença: ')
    lst = stç.split()
    soma = 0

    for i in lst:
        soma += len(i)
        med = soma/len(lst) 
    
    print(f'{med:3.1f}')