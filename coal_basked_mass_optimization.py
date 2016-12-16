def pack_basket(basket,pile):

    import itertools
    import string

    pile_list = pile.split(' ')
    mass_list = []

    pile_list_num = []

    for i in pile_list:
        replace = i.translate(None, 'dust')
        pile_list_num.append(replace)
#        all=string.maketrans('','')
#        nodigs=all.translate(all, string.digits)
#        pile_list_num.append(i.translate(all, nodigs))

    for i in pile_list_num:
        if i.isdigit() == True:
            mass_list.append(int(i))
    print mass_list

    mass = 0
    combos_list = []

    if mass_list == []:
        pass
    else:
        for i in range(0, len(mass_list)+1):
            for j in itertools.combinations(mass_list, i):
                combos_list.append(list(j))
        for i in combos_list:
            total = sum(i)
            if total <= basket and total > mass:
                mass = total

    return 'The basket weighs ' + str(mass) + ' kilograms'
        
