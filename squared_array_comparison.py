def comp(array1, array2):

    print array1
    print array2

    if array1 == None or array2 == None:
        return False

    from sets import Set

    array1_sqr = []

    for i in array1:
        array1_sqr.append(i**2)

    array1_sqr = Set(array1_sqr)
    array2 = Set(array2)

    array1_sqr = list(array1_sqr)
    array2 = list(array2)

    array1_sqr.sort()
    array2.sort()

    print array1_sqr
    print array2

    if array2 == array1_sqr:
        return True
    else:
        return False


	
