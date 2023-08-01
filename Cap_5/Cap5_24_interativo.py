def case(index):
    for i in index[0]:
        if index[0].isnumeric():
            print('Unknown')
        elif index[0].isupper():
            print('Capitalized')
        else:
            print('Lower')