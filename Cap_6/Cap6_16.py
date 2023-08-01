mult3 = []
mult5 = []
mult7 = []

for i in range(100):
    if i%3 == 0:
        mult3.append(i)
print(mult3)
print()

for i in range(100):
    if i%5 == 0:
        mult5.append(i)
print(mult5)
print()

for i in range(100):
    if i%7 == 0:
        mult7.append(i)
print(mult7)
print()

#item a
mult35 = []
for i in range(100):
    if i%35 == 0:
        mult35.append(i)
print(mult35)
print()

#item b 
mult105 = []
for i in range(100):
    if i%35 == 0:
        mult105.append(i)
print(mult105)
print()

#item c
print(set(mult3) | set(mult7))
print()

#item d
print(set(mult3) - set(mult7))
print()

#item e 
print(set(mult7) - set(mult3))
print()
