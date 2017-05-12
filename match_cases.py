def find_children(dancing_brigade):

    ls = list(dancing_brigade)

    lower = []
    upper = []

    for i in ls:
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)
    upper.sort()

    op_ls = []

    for i in upper:
        op_ls.append(i)
        for index, j in enumerate(lower):
            check = i.lower()
            if check == j:
                op_ls.append(j)
    return ''.join(op_ls)
