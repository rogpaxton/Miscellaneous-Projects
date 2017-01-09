def part(n):

    from operator import mul
    import numpy


    def partition(m):
        answer = set()
        answer.add((m, ))
        for x in range(1, m):
            for y in partition(m - x):
                answer.add(tuple(sorted((x, ) + y)))
        return answer

    answer = partition(n)
    np_set = numpy.empty(0)
    for i in list(answer):
        np_set = numpy.insert(np_set, 0, reduce(mul, i))
    np_set = numpy.unique(np_set)
    np_set = numpy.sort(np_set)

    ranger = str(int(numpy.ptp(np_set)))
    average = '%.2f' % (numpy.mean(np_set))
    medianer = '%.2f' % numpy.median(np_set)

    return "Range: " + ranger + " Average: " + average + " Median: " + medianer
