def ant(grid, column, row, n, direction = 0):

    print(grid, column, row, n, direction)


    dirs = [0, 1, 2, 3]

    dir = direction

    for i in range(n):
        if grid[row][column] == 1:
            dir += 1
            if dir > 3:
                dir = 0
        elif grid[row][column] == 0:
            dir -= 1
            if dir < 0:
                print('good')
                dir = 3

        if grid[row][column] == 0:
            grid[row][column] = 1
        elif grid[row][column] == 1:
            grid[row][column] = 0

        if dir == 0 and row == 0:
            grid.insert(0, [0]*len(grid[0]))
        elif dir == 1 and column == len(grid[0])-1:
            for i in grid:
                i.append(0)
        elif dir == 2 and row == len(grid) - 1:
            grid.append([0]*len(grid[0]))
        elif dir == 3 and column == 0:
            for i in grid:
                i.insert(0, 0)


        if dir == 0:
            row -= 1
            if row == -1:
                row = 0
        elif dir == 1:
            column += 1
        elif dir == 2:
            row += 1
        elif dir == 3:
            column -= 1
            if column == -1:
                column = 0

        print(grid, row, column, dir)
    return(grid)
