#esta questão eu não cosegui encontar o resultado do livro.
key = 'ABBFHDL'
acc = 0

for i in range(1, len(key)):
        if key[i] < key[i-1]:
                acc += 1
        
print(acc)