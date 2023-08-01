def stats(file):
    file1 = open(file,'r')
    cont = file1.read()
    file1.close()
    cont_pala = cont.split()
    cont2 = cont.split('\n')
    print(f'linhas: {len(cont2)}')
    print(f'Palavras: {len(cont_pala)}')
    print(f'Caracter: {len(cont)}')



