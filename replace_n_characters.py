def replace_nth(text, n, old, new):

    text_lst = list(text)
    counter = 0

    for index, i in enumerate(text_lst):
        if i == old:
            counter += 1
        if i == old and n <= 0:
            pass
        elif i == old and counter != 0 and counter%n == 0:
            text_lst[index] = new

    return ''.join(text_lst)
            
