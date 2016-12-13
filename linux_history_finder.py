def bang_contain_string(s,history):

    s_str = str(s)

    hist_list = history.split('\n')

    short_list = []

    for i in hist_list:
        checker = i.split('  ')
        if len(checker) == 3:
            checker = [5] + checker
        checker.remove(checker[0])
        checker.remove(checker[0])
        checker.remove(checker[0])
        insert = checker
        checker3 = checker[0]
        if s_str in str(checker3):
            short_list.append(str(insert[0]))


    length = len(short_list)

    if short_list == []:
        short_list.append("!" + s + ": event not found")

    op = str(short_list[length - 1])
    return op
        
