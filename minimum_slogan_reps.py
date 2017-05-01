def slogans(p,r):
    chars = list(p)

    chars.reverse()

    combos = [[chars[0]]]

    for index, i in enumerate(chars):
        if index == 0:
            pass
        else:
            adder = list(combos[index - 1])
            adder.append(i)
            combos.append(adder)

    heard = list(r)

    heard.reverse()

    rep_list = []

    reps = 1

    to_pop = []

    for index, i in enumerate(heard):
        rep_list.append(i)
        if rep_list in combos:
#            to_pop.append(index)
            pass
        else:
            print rep_list
            reps += 1
#            rep_list = [heard[index]]
            if heard[index] == chars[0]:
                rep_list = [heard[index]]
            else:
                rep_list = [chars[0], heard[index]]


    return reps
