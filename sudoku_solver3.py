def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""

    options = [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]
#    while 0 in [item for sublist in puzzle for item in sublist]:
    for index1, i in enumerate(puzzle):
        for index2, j in enumerate(i):
            if j == 0:
                options[index1][index2] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                options[index1][index2] = j
    for index1, i in enumerate(options):
        for index2, j in enumerate(i):
            if isinstance(options[index1][index2], list) == False:
                for k in i:
                    if k != options[index1][index2] and isinstance(k, list) and options[index1][index2] in k:
                        k = k.remove(options[index1][index2])

    print options







    return puzzle
