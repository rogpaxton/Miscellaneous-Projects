def validBraces(string):

    chars = list(string)

    cont = 1

    while cont == 1:
        print cont
        print chars
        cont = 0
        for index, i in enumerate(chars):
            if index < len(chars)-1:
                if i =='(' and chars[index+1] == ')':
                    chars.pop(index)
                    chars.pop(index)
                    cont = 1
                elif i =='[' and chars[index+1] == ']':
                    chars.pop(index)
                    chars.pop(index)
                    cont = 1
                elif i =='{' and chars[index+1] == '}':
                    chars.pop(index)
                    chars.pop(index)
                    cont = 1

    if cont == 0 and len(chars) > 0:
        return False
    else:
        return True
