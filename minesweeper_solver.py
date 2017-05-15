def solve_mine(map, n):

    rows = map.split('\n')
    grid = [i.split() for i in rows]

    for i in grid:
        print i
    print '*****'

    for index, i in enumerate(grid):
        for index2, j in enumerate(i):
            if j == '0':
                if index > 0 and index < (len(grid)-1) and index2 > 0 and index2 < (len(i)-1):
                    grid[index-1][index2-1] = str(open(index-1, index2-1))
                    grid[index-1][index2] = str(open(index-1, index2))
                    grid[index-1][index2+1] = str(open(index-1, index2+1))
                    grid[index][index2+1] = str(open(index, index2+1))
                    grid[index][index2-1] = str(open(index, index2-1))
                    grid[index+1][index2-1] = str(open(index+1, index2-1))
                    grid[index+1][index2] = str(open(index+1, index2))
                    grid[index+1][index2+1] = str(open(index+1, index2+1))
                elif index == 0 and index < (len(grid)-1) and index2 > 0 and index2 < (len(i)-1):
                elif index == 0 and index < (len(grid)-1) and index2 > 0 and index2 < (len(i)-1):
                elif index == 0 and index < (len(grid)-1) and index2 > 0 and index2 < (len(i)-1):
                elif index > 0 and index < (len(grid)-1) and index2 > 0 and index2 < (len(i)-1):
                elif index > 0 and index < (len(grid)-1) and index2 > 0 and index2 < (len(i)-1):
                elif index > 0 and index < (len(grid)-1) and index2 > 0 and index2 < (len(i)-1):
                elif index > 0 and index < (len(grid)-1) and index2 > 0 and index2 < (len(i)-1):


    
