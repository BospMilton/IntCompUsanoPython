def par(lst1,lst2,c):
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i]+lst2[j] == c:
                print(lst1[i], lst2[j])
