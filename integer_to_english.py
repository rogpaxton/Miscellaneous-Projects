def int_to_english(n):

    digit_list = list(str(n))
    digit_list.reverse()

    count = 0

    triplet_list=[]
    while count<len(digit_list):
          triplet_list.append(digit_list[count:count+3])
          count+=3

    for i in triplet_list:
        i.reverse()

    power = 0

    op_list = []

    while len(triplet_list) > 0:
        for i in triplet_list:
            if len(i) == 1:
                i.insert(0, '0')
                i.insert(0, '0')
            elif len(i) == 2:
                i.insert(0, '0')

            if i[0] == '1':
                op_list.append('one hundred')
            elif i[0] == '2':
                op_list.append('two hundred')
            elif i[0] == '3':
                op_list.append('three hundred')
            elif i[0] == '4':
                op_list.append('four hundred')
            elif i[0] == '5':
                op_list.append('five hundred')
            elif i[0] == '6':
                op_list.append('six hundred')
            elif i[0] == '7':
                op_list.append('seven hundred')
            elif i[0] == '8':
                op_list.append('eight hundred')
            elif i[0] == '9':
                op_list.append('nine hundred')

            if i[1] == '0':
                if i[2] == '0':
                    pass
                elif i[2] == '1':
                    op_list.append('one')
                elif i[2] == '2':
                    op_list.append('two')
                elif i[2] == '3':
                    op_list.append('three')
                elif i[2] == '4':
                    op_list.append('four')
                elif i[2] == '5':
                    op_list.append('five')
                elif i[2] == '6':
                    op_list.append('six')
                elif i[2] == '7':
                    op_list.append('seven')
                elif i[2] == '8':
                    op_list.append('eight')
                elif i[2] == '9':
                    op_list.append('nine')
            elif i[1] == '1':
                if i[2] == '0':
                    op_list.append('ten')
                elif i[2] == '1':
                    op_list.append('eleven')
                elif i[2] == '2':
                    op_list.append('twelve')
                elif i[2] == '3':
                    op_list.append('thirteen')
                elif i[2] == '4':
                    op_list.append('fourteen')
                elif i[2] == '5':
                    op_list.append('fifteen')
                elif i[2] == '6':
                    op_list.append('sixteen')
                elif i[2] == '7':
                    op_list.append('seventeen')
                elif i[2] == '8':
                    op_list.append('eighteen')
                elif i[2] == '9':
                    op_list.append('nineteen')
            elif i[1] == '2':
                op_list.append('twenty')
                if i[0] == '0':
                    pass
                elif i[2] == '1':
                    op_list.append('one')
                elif i[2] == '2':
                    op_list.append('two')
                elif i[2] == '3':
                    op_list.append('three')
                elif i[2] == '4':
                    op_list.append('four')
                elif i[2] == '5':
                    op_list.append('five')
                elif i[2] == '6':
                    op_list.append('six')
                elif i[2] == '7':
                    op_list.append('seven')
                elif i[2] == '8':
                    op_list.append('eight')
                elif i[2] == '9':
                    op_list.append('nine')
            elif i[1] == '3':
                op_list.append('thirty')
                if i[0] == '0':
                    pass
                elif i[2] == '1':
                    op_list.append('one')
                elif i[2] == '2':
                    op_list.append('two')
                elif i[2] == '3':
                    op_list.append('three')
                elif i[2] == '4':
                    op_list.append('four')
                elif i[2] == '5':
                    op_list.append('five')
                elif i[2] == '6':
                    op_list.append('six')
                elif i[2] == '7':
                    op_list.append('seven')
                elif i[2] == '8':
                    op_list.append('eight')
                elif i[2] == '9':
                    op_list.append('nine')
            elif i[1] == '4':
                op_list.append('forty')
                if i[2] == '0':
                    pass
                elif i[2] == '1':
                    op_list.append('one')
                elif i[2] == '2':
                    op_list.append('two')
                elif i[2] == '3':
                    op_list.append('three')
                elif i[2] == '4':
                    op_list.append('four')
                elif i[2] == '5':
                    op_list.append('five')
                elif i[2] == '6':
                    op_list.append('six')
                elif i[2] == '7':
                    op_list.append('seven')
                elif i[2] == '8':
                    op_list.append('eight')
                elif i[2] == '9':
                    op_list.append('nine')
            elif i[1] == '5':
                if i[0] == '0':
                    pass
                elif i[2] == '1':
                    op_list.append('one')
                elif i[2] == '2':
                    op_list.append('two')
                elif i[2] == '3':
                    op_list.append('three')
                elif i[2] == '4':
                    op_list.append('four')
                elif i[2] == '5':
                    op_list.append('five')
                elif i[2] == '6':
                    op_list.append('six')
                elif i[2] == '7':
                    op_list.append('seven')
                elif i[2] == '8':
                    op_list.append('eight')
                elif i[2] == '9':
                    op_list.append('nine')
            elif i[1] == '6':
                op_list.append('sixty')
                if i[0] == '0':
                    pass
                elif i[2] == '1':
                    op_list.append('one')
                elif i[2] == '2':
                    op_list.append('two')
                elif i[2] == '3':
                    op_list.append('three')
                elif i[2] == '4':
                    op_list.append('four')
                elif i[2] == '5':
                    op_list.append('five')
                elif i[2] == '6':
                    op_list.append('six')
                elif i[2] == '7':
                    op_list.append('seven')
                elif i[2] == '8':
                    op_list.append('eight')
                elif i[2] == '9':
                    op_list.append('nine')
            elif i[1] == '7':
                op_list.append('seventy')
                if i[0] == '0':
                    pass
                elif i[2] == '1':
                    op_list.append('one')
                elif i[2] == '2':
                    op_list.append('two')
                elif i[2] == '3':
                    op_list.append('three')
                elif i[2] == '4':
                    op_list.append('four')
                elif i[2] == '5':
                    op_list.append('five')
                elif i[2] == '6':
                    op_list.append('six')
                elif i[2] == '7':
                    op_list.append('seven')
                elif i[2] == '8':
                    op_list.append('eight')
                elif i[2] == '9':
                    op_list.append('nine')
            elif i[1] == '8':
                op_list.append('eight')
                if i[0] == '0':
                    pass
                elif i[2] == '1':
                    op_list.append('one')
                elif i[2] == '2':
                    op_list.append('two')
                elif i[2] == '3':
                    op_list.append('three')
                elif i[2] == '4':
                    op_list.append('four')
                elif i[2] == '5':
                    op_list.append('five')
                elif i[2] == '6':
                    op_list.append('six')
                elif i[2] == '7':
                    op_list.append('seven')
                elif i[2] == '8':
                    op_list.append('eight')
                elif i[2] == '9':
                    op_list.append('nine')
            elif i[1] == '9':
                op_list.append('ninety')
                if i[0] == '0':
                    pass
                elif i[2] == '1':
                    op_list.append('one')
                elif i[2] == '2':
                    op_list.append('two')
                elif i[2] == '3':
                    op_list.append('three')
                elif i[2] == '4':
                    op_list.append('four')
                elif i[2] == '5':
                    op_list.append('five')
                elif i[2] == '6':
                    op_list.append('six')
                elif i[2] == '7':
                    op_list.append('seven')
                elif i[2] == '8':
                    op_list.append('eight')
                elif i[2] == '9':
                    op_list.append('nine')

        triplet_list.pop(0)

    op = ' '.join(op_list)
    print op
    return op
