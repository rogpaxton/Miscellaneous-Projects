def bouncingBall(h, bounce, window):
    print h
    print bounce
    print window

    counter = 1

    if window >= h or window <= 0 or h <= 0 or bounce >= 1 or bounce <= 0:
        return -1

    h *= bounce

    while h > window:
        h *= bounce
        counter += 2

    return counter
