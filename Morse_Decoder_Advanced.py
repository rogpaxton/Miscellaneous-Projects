def decodeBits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = bits.strip('0')
    print bits
    bits_lst = list(bits)
    print MORSE_CODE

#determine transmission rate
    zed_counter = 0
    zed_min = 1000
    uno_counter = 0
    uno_min = 1000

    for i in bits_lst:
        if i == '0':
            zed_counter += 1
            if uno_counter > 0 and uno_counter < uno_min:
                uno_min = uno_counter
            uno_counter = 0
        elif i == '1':
            uno_counter += 1
            if zed_counter > 0 and zed_counter < zed_min:
                zed_min = zed_counter
            zed_counter = 0

    trans_rate = 1
    if zed_min < uno_min:
        trans_rate = zed_min
    else:
        trans_rate = uno_min

#build reduce bits list
    red_lst = []

    for index, i in enumerate(bits_lst):
        if index%trans_rate == 0:
            red_lst.append(i)

#convert 1s to dots and dashes
    uno_counter = 0
    transc = []
    for i in red_lst:
        if i == '1':
            uno_counter += 1
        if i == '0':
            if uno_counter == 1:
                transc.append('.')
            if uno_counter == 3:
                transc.append('-')
            uno_counter = 0
            transc.append(' ')

    print transc

    if len(red_lst) > 1 and red_lst[-1] == '1' and red_lst[-2] == '0':
        transc.append('.')
    elif len(red_lst) > 3 and red_lst[-1] == '1' and red_lst[-2] == '1' and red_lst[-3] == '1' and red_lst[-4] == '0':
        transc.append('-')
    elif red_lst == ['1']:
        transc.append('.')


    deciphered = ''.join(transc)

    return deciphered


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
