import math

fstrg_a = 'a)_ pi = {:3.1f}, e = {:3.1f}'
fstrg_b = 'b)_ pi = {:3.2f}, e = {:3.2f}'
fstrg_c = 'c)_ pi = {:3.6e}, e = {:3.6e}'
fstrg_d = 'd)_ pi = {:3.5f}, e = {:3.5f}'

print(fstrg_a.format(math.pi, math.e))
print(fstrg_b.format(math.pi, math.e))
print(fstrg_c.format(math.pi, math.e))
print(fstrg_d.format(math.pi, math.e))