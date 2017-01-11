def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""

#    while 0 in [item for sublist in puzzle for item in sublist]:
    hor_lst = []
    vert_lst = []

    for i in range(1, 10):
        hor_lst_ind = []
        vert_lst_ind = []
        vert_lst_temp = []
        for j in puzzle:
            if i in j:
                pass
            else:
                hor_lst_ind.append(puzzle.index(j))
        hor_lst.append(hor_lst_ind)
        for j in range(0, 10):
            for k in puzzle:
                vert_lst_temp.append(k[j])
            if i in vert_lst_temp:
                pass
            else:
                vert_lst.append(j)
    print vert_list
            else:
    return puzzle
