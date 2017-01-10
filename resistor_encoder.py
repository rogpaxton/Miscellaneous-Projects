def encode_resistor_colors(ohms_string):

    color_dict = {'0': 'black', '1': 'brown', '2': 'red', '3': 'orange', '4': 'yellow', '5': 'green', '6': 'blue', '7': 'violet', '8': 'gray', '9': 'white'}

    ohms_lst = list(ohms_string)

    num_lst = []

    for i in ohms_lst:
        if i.isdigit() or i == '.':
            num_lst.append(i)

    num = float(''.join(num_lst))

    if 'k' in ohms_lst:
        num *= 1000
    elif 'M' in ohms_lst:
        num *= 1000000

    num_int = int(num)

    num_lst2 = list(str(num_int))

    op_lst = [color_dict[num_lst2[0]], color_dict[num_lst2[1]]]

    op_lst.append(color_dict[str(len(num_lst2)-2)])

    op_lst.append('gold')

    return ' '.join(op_lst)



    # your code here
