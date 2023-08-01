def mmedia(lst):
    med_a = []
    med_t = 0
    for i in range(len(lst)):
        med_a.append(sum(lst[i])/3)
    #média da turma
    med_t = sum(med_a)/len(med_a)    
    return med_a, med_t

