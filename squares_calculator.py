def list_squared(m, n):

    from math import sqrt
    from sets import Set

    final_list = []

    if m > 1:
        final_list = []
    else:
        final_list = [[1, 1]]

    for i in range(m, n+1):
        div_set = Set()
        sum_square = 0

        div_set = Set(j for j in range(1, i+1) if i%j == 0)

        for k in div_set:
            sum_square += k**2
        if sum_square%2 == 0 and sqrt(sum_square) - int(sqrt(sum_square)) == 0:
            final_list.append([i, sum_square])

    return final_list
    
