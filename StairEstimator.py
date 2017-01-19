def stairs_in_20(stairs):
    sum = 0

    for i in stairs:
        for j in i:
            sum += j

    return sum*20
