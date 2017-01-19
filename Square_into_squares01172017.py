def decompose(n):

    from itertools import combinations

    sqr_lst = [i**2 for i in range(1,n)]

    result = [seq for i in range(len(sqr_lst), 0, -1) for seq in combinations(sqr_lst, i) if sum(seq) == n**2]

    final = [0]
    for i in result:
        if list(i)[-1] > final[-1]:
            final = list(i)

    master_lst = []
    for i in final:
        master_lst.append(int(i**(0.5)))


    return master_lst
