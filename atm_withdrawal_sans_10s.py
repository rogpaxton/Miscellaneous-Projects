def withdraw(n):

    bills = []

    if n % 20 == 0:
        bills.append(n/100)
        n -= bills[0] * 100
        bills.append(0)
        bills.append(n/20)
    else:
        new_n = n
        bills.append(new_n/100)
        new_n -= bills[0] * 100
        if new_n / 50 == 0:
            bills.append(1)
        else:
            bills.append(0)
        new_n -= bills[1]*50
        bills.append(new_n/20)
        new_n -= bills[2] * 20
        if new_n > 0:
            bills[0] -= 1
            bills[1] += 1
            bills[2] = 0
        new_n = bills[0]*100 + bills[1]*50 + bills[2]*20
        diff = n - new_n
        bills[2] = diff/20

    print bills
    return bills



    return bills
