def pac_man(N, PM, enemies):

    fnl_matrix_size = [N, N]

    if N == 1:
        return 0

    if enemies == []:
        return N * N - 1

    upper_limit = 0
    lower_limit = N
    left_limit = 0
    right_limit = N

    for i in enemies:
        if i[0] > upper_limit and i[0] > PM[0]:
            upper_limit = i[0]
        elif i[0] < lower_limit and i[0] < PM[0]:
            lower_limit = i[0]

        if i[1] > left_limit and i[1] > PM[1]:
            left_limit = i[1]
        elif i[1] < right_limit and i[1] < PM[1]:
            right_limit = i[1]

    op = (lower_limit - upper_limit) * (right_limit - left_limit)
    print op
    return op
    
