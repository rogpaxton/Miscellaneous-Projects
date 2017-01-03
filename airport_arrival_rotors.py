def flap_display(lines, rotors):

    lines_char_list = []
    for i in lines:
        lines_char_list.append(list(i))
    alpha_list = list(ALPHABET)
    op_list = []

    for i, k in zip(lines_char_list, rotors):
        new_list = []
        for index,j in enumerate(i):
            init_pos = int(alpha_list.index(j))
            new_pos = init_pos + sum(k[0:index+1])
            if new_pos > len(alpha_list):
                new_pos = new_pos - ((new_pos/len(alpha_list)) * len(alpha_list))
            if new_pos == 54:
                new_pos = 0
            new_list.append(alpha_list[new_pos])
        new_entry = ''.join(new_list)
        op_list.append(new_entry)

    return op_list
