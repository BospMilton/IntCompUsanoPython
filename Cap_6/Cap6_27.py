lst = ['Jesus', 'Deus']
file = open('Livro.txt','r',encoding='UTF-8')
for num_linha, linha in enumerate(file, start=1):
    linha = linha.strip()
    for palavra in lst:
        if palavra in linha:
            print(f"'{palavra}' - {num_linha}")

            