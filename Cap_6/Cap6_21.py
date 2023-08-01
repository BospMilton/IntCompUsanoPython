
dsc = {}
file = open('nasdaq.txt','r')
lines = file.readlines()

for i in range(0, len(lines), 2):
            key = lines[i].strip()  
            value = lines[i + 1].strip()
            dsc[key] = value
while True:
        imp = input('Digite o nome de uma empresa: ')
        print(dsc[imp])

