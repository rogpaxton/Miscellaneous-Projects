def next_gen(cells):

    from scipy.ndimage import convolve

    print cells

    if cells == []:
        return []

    kernel = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

    trainer = convolve(cells, kernel, mode='constant')

    print trainer

    trained = [[0 for col in range(len(cells[0]))] for row in range(len(cells))]

    for index_y, i in enumerate(trained):
        for index_x, j in enumerate(i):
            if cells[index_y][index_x] == 1 and trainer[index_y][index_x] < 2:
                trained[index_y][index_x] = 0
            elif cells[index_y][index_x] == 1 and trainer[index_y][index_x] == 2 or trainer[index_y][index_x] == 3:
                trained[index_y][index_x] = 1
            elif cells[index_y][index_x] == 1 and trainer[index_y][index_x] > 3:
                trained[index_y][index_x] = 0
            if cells[index_y][index_x] == 0 and trainer[index_y][index_x] == 3:
                trained[index_y][index_x] = 1

    print trained

    return trained

    
