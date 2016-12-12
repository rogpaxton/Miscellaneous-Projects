def is_polydivisible(s, b):

    digit_list = list(s)
    list_len = len(digit_list) + 1
    list_power = range(1, list_len)
    list_power.reverse()
    base_10 = 0

    for i, j in zip(digit_list, list_power):
        base_10 += int(i)*(b**j)

    decider = 0

    base_10_list = [int(x) for x in str(base_10)]
    calc_list = []

    n = 1

    for i in base_10_list:
        calc_list.append(str(i))
        calc = int(''.join(calc_list))
        print calc
        if calc % n != 0:
            decider += 1
        n += 1

    if decider == 0:
        return True
    else:
        return False

def get_polydivisible(n, b):

    next = 0
    valid_polys = []

    while len(valid_polys) < n:
        if next%(len(list(str(next)))) == 0:
            valid_polys.append(next)
        next += 1

    valid_polys.reverse()
    print valid_polys

    val = valid_polys[0]

    if b == 10:
        op = val
    else:
        num_rep={10:'A',
         11:'B',
         12:'C',
         13:'D',
         14:'E',
         15:'F',
         16:'G',
         17:'H',
         18:'I',
         19:'J',
         20:'K',
         21:'L',
         22:'M',
         23:'N',
         24:'O',
         25:'P',
         26:'Q',
         27:'R',
         28:'S',
         29:'T',
         30:'U',
         31:'V',
         32:'W',
         33:'X',
         34:'Y',
         35:'Z',
         36:'a',
         37:'b',
         38:'c',
         39:'d',
         40:'e',
         41:'f',
         42:'g',
         43:'h',
         44:'i',
         45:'j',
         46:'k',
         47:'l',
         48:'m',
         49:'n',
         50:'o',
         51:'p',
         52:'q',
         53:'r',
         54:'s',
         55:'t',
         56:'u',
         57:'v',
         58:'w',
         59:'x',
         60:'y',
         61:'z'}
        new_num_string=''
        current=val
        while current!=0:
            remainder=current%n
            if 72>remainder>9:
                remainder_string=num_rep[remainder]
            elif remainder>=72:
                remainder_string='('+str(remainder)+')'
            else:
                remainder_string=str(remainder)
            new_num_string=remainder_string+new_num_string
            current=current/n
        op = new_num_string

    return str(op)
