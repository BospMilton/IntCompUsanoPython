import re

file1 = open('Livro.txt','r', encoding='UTF-8')
file2 = open('Dicionario.txt','w', encoding='UTF-8')
cont = file1.read()
word = re.findall(r'\b\w+\b', cont.lower())
word_f = sorted(set(word))
for i in word_f:
    if len(i)<=2:
        word_f.remove(i)
for word in word_f:
    file2.write(word + '\n')

