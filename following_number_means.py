def averages(arr):

    print arr

    if arr == None:
        return []

    if len(arr) <= 1:
        return []

    op_lst = []

    for index, i in enumerate(arr[:-1]):
        op_lst.append((float(i)+float(arr[index+1]))/2)

    return op_lst
