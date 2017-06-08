def soundex(name):
    print(name)

    word_lst = name.split(' ')

    char_lst = []

    for i in word_lst:
        char_lst.append(list(i))

    for i in char_lst:
        for index,j in enumerate(i):
            if index == 0:
                pass
            else:
                if j == ('h') or j == ('w') or j == ('a') or j == ('e') or j == ('i') or j == ('o') or j == ('u') or j == ('y'):
                    i[index] = 0

    for i in char_lst:
        i[:] = [item for item in i if item != 0]

    for i in char_lst:
        for index,j in enumerate(i):
            if j == ('b') or j == ('f') or j == ('p') or j == ('b'):
                i[index] = 1
            elif j == ('c') or j == ('g') or j == ('k') or j == ('q') or j == ('s') or j == ('x') or j == ('z'):
                i[index] = 2
            elif j == ('d') or j == ('t'):
                i[index] = 3
            elif j == ('l'):
                i[index] = 4
            elif j == ('m') or j == ('n'):
                i[index] = 5
            elif j == ('r'):
                i[index] = 6

    char_lst2 = []

    for i in char_lst:
        temp = []
        for index,j in enumerate(i[0:]):
            if len(i) == 1:
                temp.append(j)
            elif j != i[index-1]:
                temp.append(j)
        char_lst2.append(temp)

    ints = []

    for i in char_lst2:
        temp = 0
        for j in i:
            if type(j) is int:
                temp += 1
        ints.append(temp)

    for index,i in enumerate(char_lst2):
        if ints[index] == 0:
            i.append(0)
            i.append(0)
            i.append(0)
        elif ints[index] == 1:
            i.append(0)
            i.append(0)
        elif ints[index] == 2:
            i.append(0)

    for i in char_lst2:
        for index,j in enumerate(i):
            if type(j) is not str:
                i[index] = str(j)
    print(char_lst2)

    for index,i in enumerate(char_lst2):
        temp = []
        if len(i) > 4:
            for j in i[0:4]:
                temp.append(j)
            char_lst2[index] = temp


    char_join = []

    for i in char_lst2:
        char_join.append(''.join(i))

#    print(' '.join(char_join))
    return ' '.join(char_join)
