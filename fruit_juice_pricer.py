def mix_fruit(arr):

    regular = ['banana', 'orange', 'apple', 'lemon', 'grapes']
    special = [ 'avocado', 'strawberry', 'mango']

    sum = 0
    num = len(arr)

    for i in arr:
        test = i.lower()
        print test
        if test in regular:
            sum += 5
        elif test in special:
            sum += 7
        else:
            sum += 9

    print float(sum)

    return round(float(sum)/float(num), 0)
