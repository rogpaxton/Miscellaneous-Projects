def max_sumDig(nMax, maxSum):

    num = 0
    numbers = []

    for i in range(nMax):
        num += 1
        if len(str(num)) <= 4:
            if num >= 1000:
                num_str = str(num)
                num_list = list(num_str)
                num_list_int = [int(x) for x in num_list]
                num_sum = sum(num_list_int)
                if num_sum <= maxSum:
                    numbers.append(num)
        else:
            for i in range(len(str(num)) - 4):
                iterator = 0

                if num >= 1000:
                    num_str = str(num)
                    num_list = list(num_str)
                    num_list_int = [num_list[iterator], num_list[iterator+1], num_list[iterator+2], num_list[iterator+3]]
                    num_sum = sum(num_list_int)
                    if num_sum <= maxSum:
                        numbers.append(num)
                iterator += 1

    num_mean = float(sum(numbers))/float(len(numbers))
    closest = min(numbers, key=lambda x:abs(x-num_mean))

    numbers_sum = sum(numbers)


    final = [len(numbers), closest, numbers_sum]

    return final
