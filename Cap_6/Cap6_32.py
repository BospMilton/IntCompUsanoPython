import random
def Manh(linha, coluna):
    pos_linha = linha // 2
    pos_coluna = coluna // 2
    visitas = {(i, j): 0 for i in range(linha) for j in range(coluna)}
    while 0 <= pos_linha < linha and 0 <= pos_coluna < coluna:
        visitas[(pos_linha, pos_coluna)] += 1
        for i in range(linha):
            for j in range(coluna):
                print(f"{visitas[(i, j)]:3}", end=" ")
            print()
        direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        delta_linha, delta_coluna = random.choice(direcoes)
        pos_linha += delta_linha
        pos_coluna += delta_coluna
