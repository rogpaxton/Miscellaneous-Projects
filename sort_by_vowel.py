def find_solutions(words):

    from sets import Set

    chars_lst = []

    for i in words:
        chars_lst.append(list(i))

    cons_lst = []

    for i in chars_lst:
        adder = []
        for j in i:
            if j != 'a' and j != 'e' and j != 'i' and j != 'o' and j != 'u':
                adder.append(j)
        cons_lst.append(adder)
        adder = []

    keepers = []
    for i in cons_lst:
        number = 0
        for j in cons_lst:
            if i == j:
                number += 1
        if number >= 5:
            keepers.append(i)

    for index, i in enumerate(keepers):
        keepers[index] = ''.join(i)

#    keepers = Set(keepers)

#    keepers = list(keepers)

    keepers_chars = []

    for i in keepers:
        keepers_chars.append(list(i))

    op_chars = []

    soln = []

    for i in keepers_chars:
        soln = []
        for j in chars_lst:
            comp = []
            for k in j:
                if k != 'a' and k != 'e' and k != 'i' and k != 'o' and k != 'u':
                    comp.append(k)
            if comp == i:
                soln.append(j)
            op_chars.append(soln)

    for i in op_chars:
        for index, j in enumerate(i):
            i[index] = ''.join(j)

    op = []

    for i in op_chars:
        if i not in op:
            op.append(i)

    print len(op)
    print op
    return op


    
