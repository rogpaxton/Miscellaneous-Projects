def valid(a):

    from sets import Set

    op = True

#each golfer plays every day

    player_set = Set()
    for i in a[0]:
        for j in i:
            lst = list(j)
            for k in lst:
                player_set.add(k)
    num_players = len(player_set)

    for i in a:
        day_lst = []
        for j in i:
            lst = list(j)
            for k in lst:
                day_lst.append(k)
        if len(day_lst) != num_players:
            return False

#number and size of groups is same every day
    number = len(a[0])
    group_size = len(list(a[0][0]))
    for i in a:
        if len(i) != number:
            return False

    for i in a:
        for j in i:
            lst = list(j)
            if len(lst) != group_size:
                return False

#each golfer plays with every other player at maximum once
    num_partners = len(a) * (len(list(a[0][0]))-1)

    for i in player_set:
        count = []
        for j in a:
            for k in j:
                if i in list(k):
                    for l in list(k):
                        count.append(l)
        if len(Set(count))-1 != num_partners:
            return False


    return op
