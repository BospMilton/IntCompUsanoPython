def espelho(texto):
    car_inv = 'BCDEFGJKLQRSZbcdefghjklqrsz'
    cont = 0
    for i in texto:
        if i in car_inv:
            cont += 1
    if cont > 0:
        print('INVALD')
    else:
        print(texto[::-1])