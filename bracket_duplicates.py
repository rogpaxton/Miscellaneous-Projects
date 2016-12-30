def string_parse(string):

    from sets import Set
    from collections import Counter

    if isinstance(string, str) == False:
        return "Please enter a valid string"

    string_lst = list(string)
    string_set = Set(string_lst)

    string_set_add = string_set.add
    string_order = []

    for i in string_lst:
        if i not in string_order:
            string_order.append(i)

    string_dict = Counter(string_lst)

    op_lst = []

    print string_dict

    for i in string_order:
        if string_dict[i] == 1:
            op_lst.append(i)
        elif string_dict[i] == 2:
            op_lst.append(i)
            op_lst.append(i)
        else:
            op_lst.append(i)
            op_lst.append(i)
            op_lst.append('[')
            for j in range(string_dict[i]-2):
                op_lst.append(i)
            op_lst.append(']')
    print op_lst

    op = ''.join(op_lst)

    return op


    
