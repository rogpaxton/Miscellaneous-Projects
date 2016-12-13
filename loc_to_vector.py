def point_vs_vector(point, vector):

    print vector
    print point

    m = (float(vector[1][1]) - float(vector[0][1]))/(float(vector[1][0]) - float(vector[0][0]))

    b = vector[0][1] - m * vector[0][0]

    print m, b

    pointer = list(point)

    op = 0

    print float(pointer[1])
    print m * pointer[0] + b

    if float(pointer[1]) == (m * pointer[0] + b):
        op = 0
    elif (m * pointer[0] + b) > pointer[1]:
        op = 1
    elif (m * pointer[0] + b) < pointer[1]:
        op = -1

    if vector[1][0] < vector [0][0]:
        op = op * -1

    print op
    return op
