def hungry_foxes(farm):

    import re
    print farm

    char_lst = list(farm)
    first_area = char_lst[0]

    areas = re.split("\[|\]", farm)

    if areas[0] == '':
        del areas[0]
    areas2 = areas

#    for index,i in enumerate(areas2):
#        if i == '':
#            del areas[index]

    print areas
    if first_area == '[':
        for index, i in enumerate(areas):
            if index%2 == 0:
                temp = list(i)
                temp.insert(0, '[')
                temp.append(']')
                areas[index] = ''.join(temp)
    else:
        for index, i in enumerate(areas):
            if index%2 != 0:
                temp = list(i)
                temp.insert(0, '[')
                temp.append(']')
                areas[index] = ''.join(temp)

    fox_out = 0
    for i in areas:
        if 'F' in i and '[' not in i:
            fox_out = 1

    for index, i in enumerate(areas):
        temp = list(i)
        new_lst = []
        if '[' in temp and 'F' in temp:
            for index2, j in enumerate(temp):
                if j == 'C':
                    temp[index2] = '.'
        elif '[' in temp and 'F' not in temp:
            pass
        else:
            if fox_out == 1:
                for index2, j in enumerate(temp):
                    if j == 'C':
                        temp[index2] = '.'
        areas[index] = ''.join(temp)

    return ''.join(areas)

            
