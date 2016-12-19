def dbl_linear(n):

    from sets import Set

    lst = [1]

    for index, i in enumerate(range(n-1)):
        x = lst[index]
        lst.append(x)
        lst.append(2 * x + 1)
        lst.append(3 * x + 1)
        lst = Set(lst)
        lst = list(lst)
        lst.sort()

    print lst[n]
    return lst[n]

	# your code
