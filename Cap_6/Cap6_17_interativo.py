def hexaASCII():
    hexa = {'a':'61', 'b':'62', 'c':'63', 'd':'64', 'e':'65', 'f':'66', 'g':'67', 
            'h':'68', 'i':'69', 'j':'6a', 'k':'6b', 'l':'6c', 'm':'6d', 'n':'6e',
            'o':'6f', 'p':'70', 'q':'71', 'r':'72', 's':'73', 't':'74', 'u':'75',
            'v':'76', 'w':'77', 'x':'78', 'y':'79', 'z':'7a'}
    while True:
        letter = input('Digite uma letra: ')
        if letter in hexa:
            print('0x{}'.format(hexa[letter]))