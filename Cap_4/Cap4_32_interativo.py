file1 = open('crypto.txt', 'r')
file2 = open('cencurado.txt','w')
cont = file1.read()
file1.close()
file2.write(' '.join('xxxx' 
                     if len(palavra) == 4 
                     else
                          palavra for palavra in cont.split())
                          )