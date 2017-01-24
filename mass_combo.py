def Guess_it(n,m):

    g = 5
    r = 4
    b = 3

    poss_g = m/g
    poss_r = m/r
    poss_b = m/b

    combos = []

    for i in range(0, poss_g+1):
        for j in range(0, poss_r+1):
            for k in range(0, poss_b+1):
                if i*g + j*r + k*b == m and i+j+k ==n:
                    new = [i, j, k]
                    combos.append(new)

    return combos
