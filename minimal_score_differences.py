def best_match(goals1, goals2):

    diff = []

    if len(goals1) > 1:
        for index, i in enumerate(goals1):
            diff.append(i - goals2[index])
    else:
        return 0

    minimum = min(diff)
    print minimum
    print diff

    idx = 0
    greatest = 0
    index = 0
    indices = []
    greatests = []

    for i in goals2:
        if diff[index] == minimum and i >= greatest:
            greatest = i
            idx = index
            indices.append(idx)
            greatests.append(i)
        index += 1

    return indices[greatests.index(max(greatests))]
#    return idx

        
