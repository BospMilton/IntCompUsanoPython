#não entendi direito o que ele quer nos dois primeiros itens, fiz como achei que era. 
lst = [-12,23,-32,40,-56]
#item a
print(f'a)_ O indice do elemento do meio é: {len(lst)//2}.')
print()

#item b
print(f'b)_ O elemento do meio é: {lst[len(lst)//2]}.')
print()


#item c
lst.sort()
lst.reverse()
print(f'c)_ A lista em ordem decrescente {lst} ')
print()

#item d
lst.append(lst[0])
lst.remove(lst[0])
print(f'd)_ Removendo o primeiro item para o ultimo lugar da lista.{lst}')
print()