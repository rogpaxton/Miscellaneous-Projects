# Exclude 'y' from vowels since it can't make up its mind if it's a vowel
vowels = 'aeiou'

def find_solutions(words):

    from collections import Counter

    letters = []
    for i in words:
        letters.append(list(i))

    consonants = []
    cons_word = []
    for i in letters:
        for j in i:
            if j != 'a' and j != 'e' and j != 'i' and j != 'o' and j != 'u':
                cons_word.append(j)
        consonants.append(cons_word)
        cons_word = []

    word_list = []

#    cnt = Counter(consonants)

#    print [k for k, v in cnt.iteritems() if v > 1]

    
