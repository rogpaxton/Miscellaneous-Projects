def sort_twisted37(arr):

    op = []
    round1 = []

    for i in arr:
        lst = list(str(i))
        for index, i in enumerate(lst):
            if i == '3':
                lst[index] = '7'
            elif i == '7':
                lst[index] = '3'
        round1.append(int(''.join(lst)))
    print round1

    round1.sort()
    round2 = []

    for i in round1:
        lst = list(str(i))
        for index, i in enumerate(lst):
            if i == '3':
                lst[index] = '7'
            elif i == '7':
                lst[index] = '3'
        round2.append(int(''.join(lst)))
    print round2

    op = round2


    return op
