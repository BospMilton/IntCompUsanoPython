#item a
flores = ['rosa', 'buganvília', 'iúca', 'margarida', 'dália', 'lírio dos vales']

print(f'a)_ {flores}')
print()

#item b
print(f'b)_ Batata esta na lista flores? {"batata" in flores}.')
print()

#item c (não podemos usar o while)
espinhosas = []
espinhosas.append(flores[0])
espinhosas.append(flores[1])
espinhosas.append(flores[2])
print(f'c)_ {espinhosas}.')
print()

#item d 
venenosas = []
venenosas.append(flores[-1])
print(f'd)_ {venenosas}.')
print()

#item e 
perigosas = espinhosas + venenosas
print(f'e)_ {perigosas}.')
print()