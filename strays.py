def stray(arr):

    arr1 = [arr[0]]
    arr2 = []

    for i in arr:
        if i not in arr1:
            arr2.append(i)
        else:
            arr1.append(i)

    if len(arr1) > len(arr2):
        return arr2[0]
    else:
        return arr1[0]

    pass
