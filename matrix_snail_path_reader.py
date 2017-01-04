def snail(array):
    ip = array
    op = []

    while ip != []:
        op.append(ip[0])
        del ip[0]
        if ip == []:
            break
        for i in ip:
            op.append(i[-1])
            del i[-1]
        ip[-1].reverse()
        op.append(ip[-1])
        del ip[-1]
        ip.reverse()
        for i in ip:
            op.append(i[0])
            del i[0]
        ip.reverse()

    op_final = []

    for i in op:
        if isinstance(i, list) == True:
            for j in i:
                op_final.append(j)
        else:
            op_final.append(i)

    return op_final
