def nome(lst):
    lst_nome = []
    lst_sobre = []
    lst_aux = []
    for i in range(len(lst)):
        lst_aux.append(lst[i].split(','))
    #preenchendo sobre nome
    y = 0 
    for i in range(len(lst_aux)):
        lst_sobre.append(lst_aux[y][0])
        y += 1
    #preenchendo nome
    for i in range(len(lst_aux)):
        lst_nome.append(lst_aux[i][1])
    #print(len(lst))    
    return lst_nome+lst_sobre
