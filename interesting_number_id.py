def is_interesting(number, awesome_phrases):

    from sets import Set

    print number
    print awesome_phrases

    number_1 = number - 1
    number_2 = number - 2

    number_list = map(int, str(number))
    number_1_list = map(int, str(number_1))
    if number_2 > 0:
        number_2_list = map(int, str(number_2))
    else:
        number_2_list = [0]
    op = 0
    op_array = [0, 0, 0, 0, 0, 0]

#zero catcher
    number_1 += 2
    number_1_list_zed = map(int, str(number_1))
    number_2 += 4
    number_2_list_zed = map(int, str(number_2))
    if len(number_list) > 2:
        if sum([i for i in number_list[1:]]) == 0:
            op_array[0] = 2
        elif sum([i for i in number_1_list_zed[1:]]) == 0:
            op_array[0] = 1
        elif sum([i for i in number_2_list_zed[1:]]) == 0:
            op_array[0] = 1
    number_1 -= 2
    number_2 -= 4

#repeated digit catcher
    number_1 += 2
    number_1_list_rep = map(int, str(number_1))
    number_2 += 4
    number_2_list_rep = map(int, str(number_2))
    if len(number_list) > 2:
        if len(Set(number_list)) == 1:
            op_array[1] = 2
#        number_1_list[len(number_1_list)-1] += 2
        if len(Set(number_1_list_rep)) == 1:
            op_array[1] = 1
#        number_2_list[len(number_2_list)-1] += 3
        if len(Set(number_2_list_rep)) == 1:
            op_array[1] = 1
#        number_1_list[len(number_1_list)-1] -= 2
#        number_2_list[len(number_2_list)-1] -= 3
    number_1 -= 2
    number_2 -= 4

#incrementing catcher
    number_1 += 2
    number_1_inc = map(int, str(number_1))
    number_2 += 4
    number_2_inc = map(int, str(number_2))
    print number_1_inc
    print number_2_inc
    if len(number_list) > 2:
        for index,i in enumerate(number_list[1:]):
            if i == 0:
                i = 10
            if i == number_list[index] + 1:
                op_array[2] = 2
            else:
                op_array[2] = 0
                break
        if op_array[2] < 2:
            for index,i in enumerate(number_1_inc[1:]):
                if i == 0:
                    i = 10
                if i == number_1_inc[index] + 1:
                    op_array[2] = 1
                else:
                    op_array[2] = 0
                    break
        if op_array[2] < 1:
            for index,i in enumerate(number_2_inc[1:]):
                if i == 0:
                    i = 10
                if i == number_2_inc[index] + 1:
                    op_array[2] = 1
                else:
                    op_array[2] = 0
                    break
    number_1 -= 2
    number_2 -= 4

#decrementing catcher
    number_1 += 2
    number_1_dec = map(int, str(number_1))
    number_2 += 4
    number_2_dec = map(int, str(number_2))
    number_list.reverse()
    number_1_dec.reverse()
    number_2_dec.reverse()
    if len(number_list) > 2:
        for index,i in enumerate(number_list[1:]):
#            if i == 0:
#                i = 10
            if i == number_list[index] + 1:
                op_array[3] = 2
            else:
                op_array[3] = 0
                break
        if op_array[3] < 2:
            for index,i in enumerate(number_1_dec[1:]):
                if i == number_1_dec[index] + 1:
                    op_array[3] = 1
                else:
                    op_array[3] = 0
                    break
        if op_array[3] < 1:
            for index,i in enumerate(number_2_dec[1:]):
                if i == number_2_dec[index] + 1:
                    op_array[3] = 1
                else:
                    op_array[3] = 0
                    break
    number_1 -= 2
    number_2 -= 4
    number_list.reverse()
#    number_1_list.reverse()
#    number_2_list.reverse()

#palindrome catcher
    if len(number_list) > 2:
        for index,i in enumerate(number_list):
            if i == number_list[len(number_list) - index - 1]:
                op_array[4] = 2
            else:
                op_array[4] = 0
                break
        number_1 += 2
        number_1_list_pal = map(int, str(number_1))
        for index,i in enumerate(number_1_list_pal):
            if op_array[4] < 2:
                if i == number_1_list_pal[len(number_1_list_pal) - index - 1]:
                    op_array[4] = 1
                else:
                    op_array[4] = 0
                    break
        number_2 += 4
        number_2_list_pal = map(int, str(number_2))
        for index,i in enumerate(number_2_list_pal):
            if op_array[4] < 1:
                if i == number_2_list_pal[len(number_2_list_pal) - index - 1]:
                    op_array[4] = 1
                else:
                    op_array[4] = 0
                    break
        number_1 -= 2
        number_2 -= 4

#awesome phrase catcher
    if number in awesome_phrases:
        op_array[5] = 2
    elif(number + 1) in awesome_phrases:
        op_array[5] = 1
    elif (number_1 + 3) in awesome_phrases:
        op_array[5] = 1
    elif (number_2 + 4) in awesome_phrases:
        op_array[5] = 1

    op = max(op_array)
    print op_array

    if len(number_list) < 3 and op_array[0] == 0:
        op = 0

    if number == 98 or number == 99:
        op = 1

    return op
