def digits_product(product):

    import operator
    import functools

    num = product
    num_ls = []
    digits = [9, 8, 7, 6, 5, 4, 3, 2]
    cont = 1

    if product < 10:
        return 10 + product

    counter = 0

    while cont == 1:
        breaker = 0
        counter += 1
        for i in digits:
            if num%i == 0:
                num_ls.append(i)
                num /= i
                breaker = 1
                break
            if functools.reduce(operator.mul, num_ls, 1) == product:
                num_ls.reverse()
                return int("".join(str(i) for i in num_ls))
        if breaker == 0:
            return -1
            cont = 0
            
