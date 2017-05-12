def count_smileys(arr):

    print arr

    count = 0

    for i in arr:
        sp = list(i)
        if len(sp) == 2:
            if (sp[0] == ':' or sp[0] == ';') and (sp[1] == ')' or sp[1] == 'D'):
                count += 1
                print sp
        if len(sp) == 3:
            if (sp[0] == ':' or sp[0] == ';') and (sp[1] == '-' or sp[1] == '~') and (sp[2] == ')' or sp[2] == 'D'):
                count += 1
                print sp
    return count
