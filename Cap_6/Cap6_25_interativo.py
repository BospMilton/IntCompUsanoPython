def dif(table):
    v_dist = set()
    for line in table:
        for index in line:
            v_dist.add(index)
    return len(v_dist)