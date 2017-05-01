def middle_permutation(string):
    from itertools import permutations

    perms = [''.join(p) for p in permutations(string)]

    perms.sort()

    print perms

    length = len(perms)

    if length % 2 != 0:
        mid = length/2
    else:
        mid = length/2 - 1

    return perms[mid]

    
