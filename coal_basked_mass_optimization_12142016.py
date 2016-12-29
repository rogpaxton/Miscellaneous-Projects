def pack_basket(basket,pile):

    from itertools import combinations
    from re import sub
    from sets import Set

    pile_list = []

    for i in pile.split(' '):
        pile_list.append(sub('[dust]', '', i))

    pile_list2 = [int(x) for x in pile_list if x and int(x) <= basket]

    sum_set = Set()

    max = 0

    for i in range(0, len(pile_list2)+1):
        for j in combinations(pile_list2, i):
            summer = sum(list(j))
            if summer > max and summer <= basket:
                max = summer
            if max == basket:
                return 'The basket weighs ' + str(max) + ' kilograms'

    return 'The basket weighs ' + str(max) + ' kilograms'
