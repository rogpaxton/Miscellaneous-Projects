def mastermind(game):

    from itertools import permutations

    colors = ["Red", "Blue", "Green", "Orange", "Purple", "Yellow"]

    colors_game = []

    answer = []

    for i in colors:
        answer.append([i, game.check([i, i, i, i])])

    idx_del = []

    for index, i in enumerate(answer):
        if i[1] == []:
            idx_del.append(index)

    idx_del.reverse()

    for i in idx_del:
        del answer[i]

    incl = []

    for i in answer:
        for j in i[1]:
            incl.append(i[0])

    perms = permutations(incl)

    for i in perms:
        print game.check(i)
        if game.check(i) == ['Black', 'Black', 'Black', 'Black']:
            return i
