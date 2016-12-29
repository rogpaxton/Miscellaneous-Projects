def validateBattlefield(field):

#correct soln; 4 @ 1, 3 @ 2, 2 @ 3, 1 @ 4, 0 > 4
    correct = [4, 3, 2, 1, 0]
    soln = [0, 0, 0, 0, 0]

    adder = 0
    x = 0
    y = 0

    for index_i, i in enumerate(field):
        for index_j, j in enumerate(i):
            if index_j == 0:
                if index_i < 9:
                    if field[index_i][index_j] == 1:
                        if field[index_i + 1][index_j + 1] == 1:
                            adder += 1
            elif index_j == 9:
                if index_i < 9:
                    if field[index_i][index_j] == 1:
                        if field[index_i + 1][index_j - 1] == 1:
                            print field[index_i + 1][index_j - 1]
                            adder += 1
            else:
                if index_i < 9:
                    if field[index_i][index_j] == 1:
                        if field[index_i + 1][index_j + 1] == 1:
                            adder += 1
                        if field[index_i + 1][index_j - 1] == 1:
                            adder += 1

    if adder > 0:
        soln[4] = 1

    adder = 0

    for index_i, i in enumerate(field):
        for index_j, j in enumerate(i):
            if j == 1:
                adder += 1
                if index_j + 1 < 10:
                    if  i[index_j + 1] == 1:
                        i[index_j + 1] = 0
                        adder += 1
                        if index_j + 2 < 10:
                            if  i[index_j + 2] == 1:
                                i[index_j + 2] = 0
                                adder += 1
                                if index_j + 3 < 10:
                                    if  i[index_j + 3] == 1:
                                        i[index_j + 3] = 0
                                        adder += 1
                                        if index_j + 4 < 10:
                                            if  i[index_j + 4] == 1:
                                                i[index_j + 4] = 0
                                                adder += 1
##############
                if index_i + 1 < 10:
                    if  field[index_i+1][index_j] == 1:
                        field[index_i+1][index_j] = 0
                        adder += 1
                        if index_i + 2 < 10:
                            if  field[index_i+2][index_j] == 1:
                                field[index_i+2][index_j] = 0
                                adder += 1
                                if index_i + 3 < 10:
                                    if  field[index_i+3][index_j] == 1:
                                        field[index_i+3][index_j] = 0
                                        adder += 1
                                        if index_i + 4 < 10:
                                            if  field[index_i+4][index_j] == 1:
                                                field[index_i+4][index_j] = 0
                                                adder += 1
##############
            if adder == 1:
                soln[0] += 1
            if adder == 2:
                soln[1] += 1
            if adder == 3:
                soln[2] += 1
            if adder == 4:
                soln[3] += 1
            if adder == 5:
                soln[4] += 1
            adder = 0

#across

#down

#check if diagonal; adjacent will show as incorrect soln automatically
    print soln
    if soln == correct:
        return True
    else:
        return False
