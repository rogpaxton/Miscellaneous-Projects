def cut_the_ropes(arr):

    from sets import Set

    arr.sort()

    remains = [len(arr)]
    count = 0

#    for i in arr:
#        if i > 0:
#            count += 1
#    remains.append(count)

    for i in arr:
        count = 0
        for index,j in enumerate(arr):
            arr[index] = j - i
        for k in arr:
            if k > 0:
                count += 1
        remains.append(count)

    remains_set = Set(remains)

    remains = list(remains_set)

    if 0 in remains:
        remains.remove(0)

    remains.sort()
    remains.reverse()

    return remains
