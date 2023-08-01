def cEasy():
    word = input('Digite uma frase: ')
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in word:
        for j in range(len(letters)):
            if j%2 == 0 and i == letters[j]:
                print(f'{letters[j+1]}',end='')
            elif j%2 != 0 and i == letters[j]:
                print(f'{letters[j-1]}',end='')
