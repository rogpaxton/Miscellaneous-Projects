def convertFracts(lst):

    from sets import Set

    denom_lst = []

    for i in lst:
        denom_lst.append(i[1])

#    def lcm(a, b):
#        if a > b:
#            greater = a
#        else:
#            greater = b

#        while True:
#            if greater % a == 0 and greater % b == 0:
#                lcm = greater
#                break
#            greater += 1

#        return lcm

#    comm_denom = reduce(lambda x, y: lcm(x, y), denom_lst)

    from fractions import gcd
#    return reduce(gcd, numbers)

    def lcm(a, b):
        return (a * b) // gcd(a, b)
    comm_denom = reduce(lambda x, y: lcm(x, y), denom_lst)
#    return reduce(lcm, numbers, 1)


#	if denom_lst and 0 not in denom_lst:
#		n = n0 = max(denom_lst)
#		denom_lst.remove(n)
#		while any( n % m for m in denom_lst ):
#			n += n0
#		comm_denom = n


    op_lst = []

    for i in lst:
        op_lst.append([(comm_denom/i[1])*i[0], comm_denom])

    return op_lst
    
