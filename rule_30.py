def rule30(list_, n):

    new_list = list_

    for i in range(n):

        translate = []

        new_list.insert(0, 0)
        new_list.insert(0, 0)
        new_list.append(0)
        new_list.append(0)

        nested = []

        i = 0

        while i<len(new_list):
            if len(new_list[i:i+3]) == 3:
                nested.append(new_list[i:i+3])
            i+=1
        print nested

        for i in nested:
            if i == [0,0,0]:
                translate.append(0)
            elif i == [0,0,1]:
                translate.append(1)
            elif i == [0,1,0]:
                translate.append(1)
            elif i == [0,1,1]:
                translate.append(1)
            elif i == [1,0,0]:
                translate.append(1)
            elif i == [1,0,1]:
                translate.append(0)
            elif i == [1,1,0]:
                translate.append(0)
            elif i == [1,1,1]:
                translate.append(0)

            new_list = translate

    return new_list
                
