def is_divisible_by_6(s):

    ls = list(s)

    idx = ls.index('*')

    combos = []

    for i in range(10):
        ls[idx] = str(i)
        temp = ''.join(ls)
        temp2 = int(temp)
        combos.append(temp2)

    op = []

    for i in combos:
        if i%6 == 0:
            op.append(i)

    op2 = []

    for i in op:
        if i == 0:
            pass
        else:
            op2.append(str(i))

    return op2
        
