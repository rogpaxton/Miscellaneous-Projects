def validSolution(board):

    for i in board:
        print i

    op = True

    x = len(board[0])/9
    y = len(board)/9

#    horizontal check

    for m in range(x):
        for i in board[9*m:9*(m+1)]:
            for j in range(1, 10):
              if j in i:
                  pass
              else:
                  return False
    print '---'

    for n in range(y):
        for i in range(len(board[0])):
            vert = []
            for j in range(9*n,9*(n+1)):
                vert.append(board[j][i])
            for k in range(1, 10):
                if k in vert:
                    pass
                else:
                    return False

    #block check
    xb = len(board)/3
    yb = len(board)/3

    for i in range(xb):
        for j in range(yb):
            block = []
            block.append(board[i*3][j*3])
            block.append(board[i*3][j*3+1])
            block.append(board[i*3][j*3+2])
            block.append(board[i*3+1][j*3])
            block.append(board[i*3+1][j*3+1])
            block.append(board[i*3+1][j*3+2])
            block.append(board[i*3+2][j*3])
            block.append(board[i*3+2][j*3+1])
            block.append(board[i*3+2][j*3+2])
            print block
            for k in range(1, 10):
                if k in block:
                    pass
                else:
                    return False

    return op
            
