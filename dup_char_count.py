def duplicate_count(text):

    text = text.lower()

    print text

    from sets import Set

    ls = list(text)

    st = Set(ls)

    greater = []

    for i in st:
        if ls.count(i) > 1:
            greater.append(i)

    return len(greater)


     
