s = ''' It was the best of times, it was the worst of times; 
it was the age of wisdom, it was the age of foolishness; 
it was the epoch of belief, it was the epoch of incredulyty; 
it was...'''

#item a
novaS = s.replace(',',' ')
novaS = novaS.replace('.',' ')
novaS = novaS.replace(';',' ')
novaS = novaS.replace('\n', ' ')
print(f'a)_ {novaS}')
print()

#item b
novaS = novaS.strip()
print(f'b)_ {novaS}')
print()

#item c
print(f'c)_ {novaS.lower()}')
print()

#item d
print(f'd)_ {novaS.count("it was")}')
print()

#item e
print(f'e)_ {novaS.replace("was","is")}')
print()

#item f
listaS = novaS.split()
print(f'f)_ {listaS}')
print()