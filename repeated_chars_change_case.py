def reverse(str):

    from itertools import groupby

    ls = ["".join(grp) for num, grp in groupby(str)]

    for index, i in enumerate(ls):
        if len(i) > 1:
            if i.isupper() == True:
                ls[index] = i.lower()
            else:
                ls[index] = i.upper()

    return ''.join(ls)
    
