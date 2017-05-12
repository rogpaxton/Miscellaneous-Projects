def increment_string(strng):

    print strng

    ls = list(strng)

    new_ls = []
    num_ls = []

    for i in ls:
        if i.isdigit() is True:
            num_ls.append(i)
        else:
            new_ls.append(i)

    if num_ls == []:
        new_ls.append('1')
        op = ''.join(new_ls)
        print op
        return op

    num = int(''.join(num_ls))
    dig_len1 = len(num_ls)
    num += 1
    dig_len2 = len(list(str(num)))

    new_num_ls = list(str(num))

    if dig_len1 > dig_len2:
        for i in range(dig_len1 - dig_len2):
            new_num_ls.insert(0, '0')

    for i in new_num_ls:
        new_ls.append(i)

    op = ''.join(new_ls)
    return op
