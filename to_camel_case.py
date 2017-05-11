def to_camel_case(text):

    import re

    if text == '':
        return ''
    elif '-' in text:
        lst = re.split(r'[-_]+', text)
#        lst = text.split('-' or '_')
        for index, i in enumerate(lst):
            lst[index] = list(i)
        for index, i in enumerate(lst):
            if index == 0:
                pass
            elif i[0].isupper():
                pass
            elif i[0].islower():
                i[0] = i[0].upper()
    elif '_' in text:
        lst = re.split(r'[-_]+', text)
        for index, i in enumerate(lst):
            lst[index] = list(i)
        for index, i in enumerate(lst):
            if index == 0:
                pass
            elif i[0].isupper():
                pass
            elif i[0].islower():
                i[0] = i[0].upper()

    for index, i in enumerate(lst):
        lst[index] = ''.join(i)

    return ''.join(lst)
                
