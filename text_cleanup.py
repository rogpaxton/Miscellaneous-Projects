def tone_it_down(string):

#lowercase
    string_list = [i.lower() for i in list(string)]

    for index, i in enumerate(string_list[:-5]):
        if i == 'g' and string_list[index+1] == 'r' and string_list[index+2] == 'u' and string_list[index+3] == 'n' and string_list[index+4] == 't':
            string_list[index] = '*'
            string_list[index+1] = '*'
            string_list[index+2] = '*'
            string_list[index+3] = '*'
            string_list[index+4] = '*'
    for index, i in enumerate(string_list[:-1]):
        if string_list[index+1] == '!':
            string_list[index+1] = '.'
        if i == '.' and string_list[index+1] == '.':
            string_list[index] = '*'
    string_list2 = filter(lambda a: a != '*', string_list)
    for index, i in enumerate(string_list2[:-1]):
        if i == ' ' and string_list[index] == ' ':
            string_list2[index] = '*'
    print string_list2
    string_list3 = filter(lambda a: a != '*', string_list2)

    string = ''.join(string_list3)
    print string

#exclamation points

#globalists

#grunt
