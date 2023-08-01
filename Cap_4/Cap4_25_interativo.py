def cvogal(str):
    cont_a = 0
    cont_e = 0
    cont_i = 0
    cont_o = 0
    cont_u = 0
    for i in str:
        if i == 'a':
            cont_a += 1
        elif i == 'e':
            cont_e += 1
        elif i == 'i':
            cont_i += 1
        elif i == 'o':
            cont_o += 1
        elif i == 'u':
            cont_u += 1
    fstr = 'a = {}, e = {}, i = {}, o = {} u= {}'
    print(fstr.format(cont_a, cont_e, cont_i, cont_o, cont_u))

