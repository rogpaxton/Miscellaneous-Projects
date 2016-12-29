def dirReduc(arr):

    num_arr = []
    for i in arr:
        if i == 'NORTH':
            num_arr.append(1)
        elif i == 'SOUTH':
            num_arr.append(-1)
        elif i == 'EAST':
            num_arr.append(2)
        elif i == 'WEST':
            num_arr.append(-2)

    ender = 0

    while ender == 0:
        for i in range(1, len(num_arr)-1):
            if num_arr[i] + num_arr[i-1] == 0:
                print i
                del num_arr[i]
                del num_arr[i-1]
                break
        if i == len(num_arr)-1:
            ender += i

    op = []
    for j in num_arr:
        if j == 1:
            op.append('NORTH')
        elif j == -1:
            op.append('SOUTH')
        elif j == 2:
            op.append('EAST')
        elif j == -2:
            op.append('WEST')
    print op
    return op
