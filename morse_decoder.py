def decodeBits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces

    bits_list = list(bits)

    min_len = 1000
    next = 1

    char_list = [bits_list[0]]
    full_list = []

    while next < len(bits_list):
        if bits_list[next - 1] == bits_list[next]:
            char_list.append(bits_list[next])
        else:
            full_list.append(char_list)
            if len(char_list) < min_len:
                min_len = len(char_list)
            char_list = []
            char_list.append(bits_list[next])
        next += 1

    dot = ['1'] * min_len * 1
    dash = ['1'] * min_len * 3
    in_char_pause = ['0'] * min_len * 1
    in_word_pause = ['0'] * min_len * 3
    tween_word_pause = ['0'] * min_len * 7

    dot_dash_list = []

    for i in full_list:
        if i == dot:

        elif i == dash:

        elif i == in_char_pause:

        elif i == in_word_pause;

        elif i == tween_word_pause:



#    return bits.replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')

def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return morseCode.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
