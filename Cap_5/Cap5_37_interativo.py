def mssl(lst):
    maior = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if sum(lst[i:j]) > maior:
                maior = sum(lst[i:j])
    return maior