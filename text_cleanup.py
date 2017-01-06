def tone_it_down(string):

    if string == '':
        return ''

    import re

    string_list = list(string)
    for index, i in enumerate(string_list):
        string_list[index] = i.lower()
        string = ''.join(string_list)

    string = string.replace('!', '')
    string = string.replace('grunt', '')

    string = re.sub('\.\.+','.', string)

    if string == '':
        return '.'

    string_list = string.split()
    counter = 0
    for index, i in enumerate(string_list):
        if i == 'globalists' and counter > 0:
            string_list[index] = 'sociopathic rich guys'
        elif i == 'globalists':
            counter += 1
        elif i == 'globalists.' and counter > 0:
            string_list[index] = 'sociopathic rich guys.'
        elif i == 'globalists.':
            counter += 1
        elif i == 'globalists,' and counter > 0:
            string_list[index] = 'sociopathic rich guys,'
        elif i == 'globalists,':
            counter += 1

    string = ' '.join(string_list)

    re.sub(' +',' ', string)

    string = string.capitalize()
    string = string.replace(' .', '.')

    if list(string)[-1] != '.':
        string = string + '.'

    return string
