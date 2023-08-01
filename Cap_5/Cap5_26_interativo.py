def dpt(jg1,jg2):
    if jg1 == jg2:
        print(0)
    elif jg1 == 'Pe' and jg2 == 'Te' or jg1 == 'Te' and jg2 == 'Pa' or jg1 == 'Pa' and jg2 == 'Pe':
        print(-1)
    elif jg2 == 'Pe' and jg1 == 'Te' or jg2 == 'Te' and jg1 == 'Pa' or jg2 == 'Pa' and jg1 == 'Pe':
        print(1)