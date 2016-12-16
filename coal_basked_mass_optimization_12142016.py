def pack_basket(basket,pile):

    import itertools
    import string
    import re

#split list on spaces
    pile_list = pile.split(' ')

#remove dust from list
    pile_list2 = []
    for i in pile_list:
        num = re.sub('[dust]', '', i)
        pile_list2.append(num)

#remove empty values from list
    pile_list3 = []
    pile_list3 = [x for x in pile_list2 if x]

#convert str to int
    pile_list4 = []
    pile_list4 = [int(x) for x in pile_list3 if x]

    pile_list5 = []
    pile_list5 = [x for x in pile_list4 if x <= basket]


    mass = 0
    combos_list = []

    if pile_list5 == []:
        pass
    else:
        for i in range(0, len(pile_list5)+1):
            for j in itertools.combinations(pile_list5, i):
                combos_list.append(list(j))
        for i in combos_list:
            total = sum(i)
            if total <= basket and total > mass:
                mass = total

    return 'The basket weighs ' + str(mass) + ' kilograms'
