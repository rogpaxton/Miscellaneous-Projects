def est_subsets(arr):
    import itertools

    n = 0

    subset_list = []

    subset_set = set(arr)
    char_list = list(subset_set)

    r = 1
    for i in char_list:
        for j in itertools.combinations(char_list, r):
            subset_list.append(j)
        r += 1
        print subset_list

    n = len(subset_list)



    return n   # n: amount of subsets that do not have repeated elements 
