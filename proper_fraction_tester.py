def proper_fractions(n):

    from fractions import Fraction

    count = 0

    for i in range(1,n):
        if Fraction(i, n).numerator == i:
            count += 1

#alternate method
#    for i in range(1,n):
#        if gcd(i,n) == 1:
#            count += 1

    return count
