def counter_effect(hit_count):

    ls = list(hit_count)
    digs = []
    op = []
    for i in ls:
        digs.append(int(i))
    for i in digs:
        if i == 0:
            op.append([0])
        else:
            temp = []
            count = 0
            for j in range(i+1):
                temp.append(count)
                count += 1
            op.append(temp)

    return op
