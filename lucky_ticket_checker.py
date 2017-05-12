def luck_check(string):
    print string
    ls = list(string)
    num_ls = []

    for i in ls:
        num_ls.append(int(i))

    ln = len(ls)

    half = ln/2

    sum1 = 0
    sum2 = 0
    for i in range(half):
        sum1 += num_ls[i]
    print sum1

    if ln%2 == 0:
        for i in range(half, ln):
            sum2 += num_ls[i]
    else:
        for i in range(half+1, ln):
            sum2 += num_ls[i]

    if sum1 == sum2:
        return True
    else:
        return False
