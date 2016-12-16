def list_squared(m, n):

    import math

    div_list = []
    sum_square = 0
    square_list = []
    add_list = []
    final_list = []

    for i in range(m, n+1):
        for j in range (1, i+1):
            if i%j == 0:
                div_list.append(j)
        for k in div_list:
            sum_square += k*k
        if math.sqrt(sum_square) - int(math.sqrt(sum_square)) == 0:
            add_list.append(i)
            add_list.append(sum_square)
            final_list.append(add_list)
            add_list = []

    print final_list
    return final_list
    
