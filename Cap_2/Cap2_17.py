#tendo como base as variaveis da questão 16
a, b = 6, 7
c = (6+7)/2
estoque = ['papel', 'grampo', 'lápis',]

#item a 
print(f'a)_ A soma de 16 mais -9 é menor do que 10? {16 + (-9) < 10}')
print()

#item b 
inv = 'inventário'
n_com = 'nomecompleto'
print(f'b)_ O comprimento da lista "inventário" é mais de cinco vezes o comprimento da string "nomecompleto"? {len(inv)//len(n_com) > 5}.')
print()

#item c (não entedi o que ele quis pergutar)
print(f'c)_ c não é maior que 24? {c>24}.')
print()

#item d (não entedi o que ele quis pergutar)
print(f'd)_ 6,75 está entre os valores de a e b? {a< 6.75 and b> 6.75}.')
print()

#item e
print(f'e)_ O comprimento da string meio é maior que o comprimento de primeiro e menor que último? {len("meio")>len("primeiro") and len("meio")< len("ultimo")}.') 
print()

#item f
print(f'f)_ A lista estoque esta vazia ou tem mais de 10 itens? {len(estoque)>10 and len(estoque) == 0}.')
print()
