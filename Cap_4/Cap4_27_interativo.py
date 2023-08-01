import shutil
def fcopy(file1,file2):
    index1 = open(file1, 'r')
    index2 = open(file2, 'w')
    shutil.copyfile(file1,file2)
    cont2 = index2.read()
    print(cont2)


