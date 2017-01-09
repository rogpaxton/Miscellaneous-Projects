def part(n):

    from operator import mul
#    import numpy as np

    def partition(m):
        answer = set()
        answer.add((m, ))
        for x in range(1, m):
            for y in partition(m - x):
                answer.add(tuple(sorted((x, ) + y)))
        return answer

    answer = partition(n)
    set_ans = set()
    for i in list(answer):
        prod = 1
#        for j in i:
#            prod *= j
#        set_ans.add(prod)
        set_ans.add(reduce(mul, i))
    list_ans = list(set_ans)
    list_ans.sort()

    ranger = str(max(list_ans) - min(list_ans))
    average = '%.2f' % (float(sum(list_ans))/float(len(list_ans)))
    if len(list_ans) == 1:
        medianer = '%.2f' % list_ans[0]
    elif len(list_ans)%2 != 0:
        medianer = '%.2f' % list_ans[len(list_ans)/2]
    else:
        medianer = '%.2f' % ((float(list_ans[len(list_ans)/2-1]) + float(list_ans[len(list_ans)/2]))/2.00)

    return "Range: " + ranger + " Average: " + average + " Median: " + medianer
    
