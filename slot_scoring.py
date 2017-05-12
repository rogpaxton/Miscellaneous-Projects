def fruit(reels, spins):

    from sets import Set
    from collections import Counter

    id1 = reels[0][spins[0]]
    id2 = reels[1][spins[1]]
    id3 = reels[2][spins[2]]

    id_ls = [id1, id2, id3]

    print id_ls

#    print id_ls

#    st = Set(id_ls)

    st = Counter(id_ls)

    if len(st) == 2 and 'King' in st and st['King'] == 2 and 'Wild' not in st:
        return 3

    if len(st) == 3:
        return 0
    elif len(st) == 1 and 'Wild' in st:
        return 100
    elif len(st) == 2 and 'Wild' in st and st['Wild'] == 2:
        return 10
    elif len(st) == 1 and 'Star' in st and st['Star'] == 3:
        return 90
    elif len(st) == 1 and 'Bell' in st and st['Bell'] == 3:
        return 80
    elif len(st) == 1 and 'Shell' in st and st['Shell'] == 3:
        return 70
    elif len(st) == 1 and 'Seven' in st and st['Seven'] == 3:
        return 60
    elif len(st) == 1 and 'Cherry' in st and st['Cherry'] == 3:
        return 50
    elif len(st) == 1 and 'Bar' in st and st['Bar'] == 3:
        return 40
    elif len(st) == 1 and 'King' in st and st['King'] == 3:
        return 30
    elif len(st) == 1 and 'Queen' in st and st['Queen'] == 3:
        return 20
    elif len(st) == 1 and 'Jack' in st and st['Jack'] == 3:
        return 10
###
    elif len(st) == 2 and 'Star' in st and st['Star'] == 2 and 'Wild' not in st:
        return 9
    elif len(st) == 2 and 'Bell' in st and st['Bell'] == 2 and 'Wild' not in st:
        return 8
    elif len(st) == 2 and 'Shell' in st and st['Shell'] == 2 and 'Wild' not in st:
        return 7
    elif len(st) == 2 and 'Seven' in st and st['Seven'] == 2 and 'Wild' not in st:
        return 6
    elif len(st) == 2 and 'Cherry' in st and st['Cherry'] == 2 and 'Wild' not in st:
        return 5
    elif len(st) == 2 and 'Bar' in st and st['Bar'] == 2 and 'Wild' not in st:
        return 4
    elif len(st) == 2 and 'King' in st and st['King'] == 2 and 'Wild' not in st:
        return 3
    elif len(st) == 2 and 'Queen' in st and st['Queen'] == 2 and 'Wild' not in st:
        return 2
    elif len(st) == 2 and 'Jack' in st and st['Jack'] == 2 and 'Wild' not in st:
        return 1
###
    elif len(st) == 2 and 'Star' in st and st['Star'] == 2 and 'Wild' in st:
        return 18
    elif len(st) == 2 and 'Bell' in st and st['Bell'] == 2 and 'Wild' in st:
        return 16
    elif len(st) == 2 and 'Shell' in st and st['Shell'] == 2 and 'Wild' in st:
        return 14
    elif len(st) == 2 and 'Seven' in st and st['Seven'] == 2 and 'Wild' in st:
        return 12
    elif len(st) == 2 and 'Cherry' in st and st['Cherry'] == 2 and 'Wild' in st:
        return 10
    elif len(st) == 2 and 'Bar' in st and st['Bar'] == 2 and 'Wild' in st:
        return 8
    elif len(st) == 2 and 'King' in st and st['King'] == 2 and 'Wild' in st:
        return 6
    elif len(st) == 2 and 'Queen' in st and st['Queen'] == 2 and 'Wild' in st:
        return 4
    elif len(st) == 2 and 'Jack' in st and st['Jack'] == 2 and 'Wild' in st:
        return 2          
