def given_nth_value(arr, k, str_):
    #your code here

    from sets import Set
    setter = Set()

    if len(arr) == 0:
        return "No values in the array"
    elif all(isinstance(item, int) for item in arr) == False:
        return "Invalid entry list"
    elif str_ != 'max':
        if str_ != 'min':
            return "Valid entries: 'max' or 'min'"
    elif isinstance(k, int) == False or k > len(Set(arr)):
        return "Incorrect value for k"
    elif str_ == 'max':
        setter = Set(arr)
        arr2 = list(setter).sort()
        return arr2[k+1]
    elif str_ == 'min':
        setter = Set(arr)
        arr2 = list(setter).sort(reverse = True)
        return arr2[k+1]

#    return "Incorrect value for k"
#    return "Valid entries: 'max' or 'min'"
#    return "No values in the array"
#    return "Invalid entry list"
#    return k-th term
