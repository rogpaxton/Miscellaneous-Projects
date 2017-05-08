def boxes_packing(length, width, height):

    box_list = []

    for index, i in enumerate(length):
        box = []
        box.append(i)
        box.append(width[index])
        box.append(height[index])
        box_list.append(box)

    for i in box_list:
        i.sort()

    box_list.sort()

    for index, i in enumerate(box_list[:-1]):
        for index2, j in enumerate(i):
            if j < box_list[index+1][index2]:
                pass
            else:
                print index
                return False

    return True




  #coding and coding..
