def decompose(n):

    from itertools import combinations

    sqr_lst = [i**2 for i in range(1,n)]

    result = [seq for i in range(len(sqr_lst), 0, -1) for seq in combinations(sqr_lst, i) if sum(seq) == n**2]

    master_lst = []
    for i in result:
        ind_lst = []
        for j in i:
            ind_lst.append(int(j**(0.5)))
        master_lst.append(ind_lst)

    op = [0]

    for i in master_lst:
        if i[:-1] > op[:-1]:
            op = i
    print op

    return op
    
