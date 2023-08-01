def crypto(name):
    file = open(name, 'r')
    cont = file.read()
    file.close()
    print(cont)
    print(cont.replace('secret', 'XXXXXX'))