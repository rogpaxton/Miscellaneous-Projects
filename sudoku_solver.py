def validSolution(board):

    op = True

    x = len(board[0])/9
    y = len(board)/9

    print x
    print y

    for i in board:
        for j in range(1, 10):
            if j in i:
                pass
            else:
                return False
    for i in range(9):
        vert = []
        for j in range(9):
            vert.append(board[j][i])
        for k in range(1, 10):
            if k in vert:
                pass
            else:
                return False
    return op
            
