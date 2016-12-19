def mix(s1, s2):

    from collections import Counter
    from operator import itemgetter
    from sets import Set

    s1_lowers = ''.join([i for i in s1 if i.islower()])
    s2_lowers = ''.join([i for i in s2 if i.islower()])

    s1_list = list(s1_lowers)
    s2_list  = list(s2_lowers)

    s1_chars = Counter(s1_list)
    s2_chars = Counter(s2_list)

    print s1_chars

    prelim = []

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in alpha:
        if s1_chars[i] > 1 or s2_chars[i] > 1:
            adder = []
            if s1_chars[i] > s2_chars[i]:
                adder.append('1')
                adder.append(i)
                adder.append(s1_chars[i])
            elif s1_chars[i] < s2_chars[i]:
                adder.append('2')
                adder.append(i)
                adder.append(s2_chars[i])
            elif s1_chars[i] == s2_chars[i]:
                adder.append('=')
                adder.append(i)
                adder.append(s1_chars[i])
            prelim.append(adder)



    ordered = prelim

    op_str = []

    for i in ordered:
        op_str.append(i[0] + ':' + i[2] * i[1])

    op_str2 = []
    for i in op_str:
        if i not in op_str2:
            op_str2.append(i)

    op_str2.sort()
    op_str2.sort(key = len, reverse = True)

    op = '/'.join(op_str2)
    print op

    return op


    
