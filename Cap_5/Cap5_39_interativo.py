def exc(pala):
    for k in range(len(pala)):
        if pala[k] in 'bcdfghjklmnpqrstvxwz':
            print(f'{pala[k]}', end='')
        elif pala[k] in 'aeiou':
            print(f'{pala[k]*4}', end='')
    print(end='!')
