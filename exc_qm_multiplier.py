def product(s):
    lst = list(s)
    print s

    exc = 0
    qm = 0

    for i in lst:
        if i == '!':
            exc += 1
        if i == '?':
            qm += 1

    return exc * qm

    pass
