def proper_fractions(n):

#    from fractions import Fraction
    from fractions import gcd
    from gc import collect
#    import fractions

    count = 0

#    evens = []
#    odds = []

#    for i in range(1, n):
#        if i%2 == 0:
#            evens.append(i)
#        else:
#            odds.append(i)

#    for i in evens:
#        if gcd(i,n) == 1:
#            count += 1
#    for i in odds:
#        if gcd(i,n) == 1:
#            count += 1

#    for i in range(1,n):
#        if Fraction(i, n).numerator == i:
#            count += 1

    for i in range(1,n):
        check = gcd(i,n)
        if check == 1:
            count += 1
        del check
        collect()

#    nums = [i for i in range(1,n) if gcd(i,n) == 1]
#    return len(nums)

#    num = 1

#    while num < n:
#        if gcd(num,n) == 1:
#            count += 1
#        num += 1

#    mult3 = filter(lambda x: gcd(x,n) == 1, xrange(1,n))

    return count
