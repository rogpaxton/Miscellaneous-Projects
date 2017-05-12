def crossover(ns, xs, ys):

    from sets import Set

    if ns == []:
        return (xs, ys)

    ns = Set(ns)
    ns = list(ns)

    if len(ns) > 1:
        if len(ns) == 2:
            if ns[0] == ns[1]:
                del ns[1]

    for i in ns:
        xsplit = xs[i:]
        ysplit = ys[i:]
        del xs[i:]
        del ys[i:]
        for j in xsplit:
            ys.append(j)
        for j in ysplit:
            xs.append(j)

    return (xs, ys)
        
