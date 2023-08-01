#nessa questão eu não consegui encontrar o resultado do livro
def parSoma(lst,num):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == num:
                print(i, j)