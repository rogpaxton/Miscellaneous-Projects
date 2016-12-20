def dbl_linear(n):

    from sets import Set

    iter_set = Set([1])
    print n
    for i in range(n):
        iter_set.add(2 * min(iter_set) + 1)
        iter_set.add(3 * min(iter_set) + 1)
        iter_set.remove(min(iter_set))

    return min(iter_set)
