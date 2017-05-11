def find(seq):

    from sets import Set

    st = Set(seq)

    seq.sort()

    step = seq[1] - seq[0]

    for i in seq:
        if (i + step) not in st:
            return (i + step)
