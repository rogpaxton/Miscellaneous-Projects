def expanded_form(num):

    num_lst = list(str(num))

    print(num_lst)

    op_lst = []

    mult = len(num_lst) - 1

    for i in num_lst:
        if i == '0':
            pass
        else:
            print(int(i) * 10**mult)
            op_lst.append(int(i) * 10**mult)
        mult -= 1

    op_lst2 = []
    for i in op_lst:
        op_lst2.append(str(i))

    return ' + '.join(op_lst2)
