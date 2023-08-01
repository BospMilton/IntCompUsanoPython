def inv_int(num):
    cent = num//100
    dez = (num // 10) % 10
    uni = num % 10
    return  print(f'{uni*100+dez*10+cent}')