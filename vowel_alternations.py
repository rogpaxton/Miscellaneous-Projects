def find_solutions(words):

    from sets import Set

    cons = []

    for i in words:
        ls = list(i)
        idx = []
        for index, j in enumerate(ls):
            if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
                idx.append(index)
            for j in idx.reverse():
                del ls[j]
            cons.append[''.join(ls)]

    st = Set(ls)

    ls_st = list(st)

#    ls_st = [[i] for i in ls_st]







    
