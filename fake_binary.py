def fake_bin(x):
    lst = list(x)
    print lst

    bin_lst = []
    for i in lst:
        if int(i) < 5:
            bin_lst.append('0')
        else:
            bin_lst.append('1')

    return ''.join(bin_lst)
        
