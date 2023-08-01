#nessa questão eu não consegui encontrar o resultado do livro
sala = 10.00 # R$/h
hora = 45 # hora # 1h - 60min
h_ext1 = hora - 40
h_ext2 = hora - 60

if hora <= 40:
    valor = sala * hora
elif hora > 40 or hora <= 60:
    valor = (sala * hora) + (h_ext1 * 1.5)
else:
    valor = (sala * hora) + (h_ext2 * 2.0)

print(valor)

