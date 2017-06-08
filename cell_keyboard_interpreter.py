def unlock(message):

    mlowers = message.lower()

    mlst = list(mlowers)

    dlst = []

    for i in mlst:
        if i == 'a' or i == 'b' or i == 'c':
            dlst.append('2')
        elif i == 'd' or i == 'e' or i == 'f':
            dlst.append('3')
        elif i == 'g' or i == 'h' or i == 'i':
            dlst.append('4')
        elif i == 'j' or i == 'k' or i == 'l':
            dlst.append('5')
        elif i == 'm' or i == 'n' or i == 'o':
            dlst.append('6')
        elif i == 'p' or i == 'q' or i == 'r' or i == 's':
            dlst.append('7')
        elif i == 't' or i == 'u' or i == 'v':
            dlst.append('8')
        elif i == 'w' or i == 'x' or i == 'y' or i == 'z':
            dlst.append('9')

    return(''.join(dlst))
