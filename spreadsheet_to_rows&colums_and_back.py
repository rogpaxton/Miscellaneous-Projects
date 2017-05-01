def spreadsheet(s):
    import re
    import string

    match = re.match(r"([a-z]+)([0-9]+)", s, re.I)
    if match:
        items = match.groups()
    print items

    nums = [re.findall(r'\d+', s)]
    print nums

    num_count = 0

    for i in items:
        if i.isdigit():
            num_count += 1
    if len(nums[0]) > 1:
        form = 'RC'
    else:
        form = 'SS'

    if form == 'RC':

        num = int(nums[0][1])
        print num

        letters = ''
        while num:
            mod = (num - 1) % 26
            letters += chr(mod + 65)
            num = (num - 1) // 26

        let_lst = list(letters)
        let_lst.reverse()
        letters = ''.join(let_lst)

#        div=int(nums[0][1])
#        string=""
#        temp=0
#        while div>0:
#            module=(div-1)%26
#            string=chr(65+module)+string
#            div=int((div-module)/26)
#        print string

        return letters + nums[0][0]

    elif form == 'SS':
#        num = 0
#        num = num * 26 + (ord(items[0].upper()) - ord('A')) + 1
#        return 'R' + items[1] + 'C' + str(num)

        num = 0
        for c in items[0]:
            if c in string.ascii_letters:
                num = num * 26 + (ord(c.upper()) - ord('A')) + 1

        return 'R' + items[1] + 'C' + str(num)        
