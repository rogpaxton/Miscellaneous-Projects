def gap(g, m, n):

    from math import sqrt

    primes_lst = []

    for num in range(m,n):
        if num%2 == 0:
            pass
        elif all(num%i!=0 for i in range(2,int(sqrt(num))+1)):
            primes_lst.append(num)
            if (primes_lst) > 1:
                if num - primes_lst[len(primes_lst)-2] == g:
                    print primes_lst
                    return [primes_lst[len(primes_lst)-2], num]

    if primes_lst == []:
        return None
