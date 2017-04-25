def socialist_distribution(population, minimum):

    reduced = []
    for i in population:
        reduced.append(i - minimum)
    improved = []
    addition = 0
    for i in reduced:
        if i < 0:
            addition -= i
            improved.append(0)
        elif i == 0:
            improved.append(0)
        else:
            improved.append(i)

    normalized = []
    for i in improved:
        normalized.append(i + minimum)

    for i in range(0,addition):
        for index, j in enumerate(normalized):
            if j == max(normalized):
                normalized[index] = j - 1
                break

    if sum(population) < (minimum * len(population)):
        return []

    return normalized
