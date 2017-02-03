def decodeBitsAdvanced(bits):

    from itertools import groupby

    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = bits.strip('0')
    print bits
    bits_lst = list(bits)

#Approximate transmission rate

    uno_max = 0
    uno_count = 1
    zed_max = 0
    zed_count = 1

    for index, i in enumerate(bits_lst[1:]):
        if i == '0' and bits_lst[index] == '0':
            zed_count += 1
        elif i == '1' and bits_lst[index] == '1':
            uno_count += 1
        if uno_count > uno_max:
            uno_max = uno_count
        if zed_count > zed_max:
            zed_max = zed_count
        if i == '0' and bits_lst[index] == '1':
            uno_count = 1
        elif i == '1' and bits_lst[index] == '0':
            zed_count = 1

    broken = ["".join(g) for k, g in groupby(bits)]

    op_lst = []




def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    word_lst = morseCode.split('       ')

    dec_lst = []
    for i in word_lst:
        chars = []
        char_lst = i.split('   ')
        for j in char_lst:
            char = j.replace(' ', '')
            chars.append(MORSE_CODE.get(char))
        dec_lst.append(chars)

    words = []
    for i in dec_lst:
        word = ''.join(i)
        words.append(word)

    op = ' '.join(words)
    return op
