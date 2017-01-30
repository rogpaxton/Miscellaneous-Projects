def decodeMorse(morseCode):

    tails_rem = morseCode.strip()

    words = tails_rem.split("   ")

    op_lst = []

    for i in words:
        letters = i.split(" ")
        for j in letters:
            op_lst.append(MORSE_CODE[j])
        op_lst.append(" ")

    op_lst.pop()

    op = ''.join(op_lst)

    return op

#    return morseCode.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
