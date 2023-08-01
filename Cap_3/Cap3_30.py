
x = int(input('Digite um número inteiro com 4 digitos: '))
print()

mil = x // 1000

cent = (x // 100) % 10

dez = (x // 10) % 10

uni = x % 10

print(mil)
print(cent)
print(dez)
print(uni)