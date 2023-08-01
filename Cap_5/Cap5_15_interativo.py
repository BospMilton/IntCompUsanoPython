def vog(n):
    for i in range(len(n)):
        if n[i] in 'aeiouAEIOU':
            return print(i, end=' ')