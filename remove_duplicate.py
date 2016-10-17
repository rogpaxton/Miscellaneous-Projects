def find_dup(arr):

    set_arr = set(arr)
    list_set = list(set_arr)

    for i in list_set:
        if i in arr:
            arr.remove(i)

    return arr[0]
