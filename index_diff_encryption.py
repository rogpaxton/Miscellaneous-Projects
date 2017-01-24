def decrypt(encrypted_text):

#Empty precheck
    if encrypted_text == "":
        return ""

#Null precheck
    if encrypted_text == None:
        return None

    chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", ":", ";", "-", "?", "!", " ", "'", "(", ")", "$", "%", "&", '"']

    text_lst = list(encrypted_text)

    dec_lst = []

#char replacement
#NOTE must start from the end and work backwards


#[0] replacement

#Check if all char valid
#Switch case

    for index, i in enumerate(dec_lst):
        if i not in chars:
            return "Exception"
        if index%2 != 0 and i.isupper():
            dec_lst[index] = i.lower()
        elif index%2 != 0 and i.islower():
            dec_lst[index] = i.upper()

    return ''.join(dec_lst)



#######################################################################
def encrypt(text):

#Empty precheck
    if text == "":
        return ""

#Null precheck
    if text == None:
        return None

    chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ",", ":", ";", "-", "?", "!", " ", "'", "(", ")", "$", "%", "&", '"']

    print "D=" + str(chars.index('D'))
    print 'o=' + str(chars.index('o'))
    print 'O=' + str(chars.index('O'))
    print '-=' + str(chars.index('-'))

    text_lst = list(text)

#Check if all char valid
#Switch case

    for index, i in enumerate(text_lst):
        if i not in chars:
            return "Exception"
        if index%2 != 0 and i.isupper():
            text_lst[index] = i.lower()
        elif index%2 != 0 and i.islower():
            text_lst[index] = i.upper()

#char replacement
    enc_lst = []
    for index, i in enumerate(text_lst[1:]):
        char_ind = chars.index(i)
        prior_ind = chars.index(text_lst[index])
        enc_lst.append(chars[prior_ind-char_ind])

#[0] replacement
    zed_index = chars.index(text_lst[0])
    enc_lst.insert(0, chars[76 - zed_index])

    return ''.join(enc_lst)
    
