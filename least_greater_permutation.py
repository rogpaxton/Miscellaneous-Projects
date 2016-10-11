def next_bigger(n):
    from itertools import permutations

    digits = str(n)

    greater_set = set(int(''.join(p)) for p in permutations(digits) if int(''.join(p)) > n)

    if len(greater_set) > 0:
        return min(greater_set)
    else:
        return -1
