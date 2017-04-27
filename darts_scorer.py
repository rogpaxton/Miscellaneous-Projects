def get_score(x,y):

    import math

    dist = math.sqrt(x*x + y*y)

    zone = 0

    if dist < (12.7/2):
        zone = 1
    elif dist > (12.7/2) and dist < (31.8/2):
        zone = 2
    elif dist > (31.8/2) and dist < (198/2):
        zone = 3
    elif dist > (198/2) and dist < (214/2):
        zone = 4
    elif dist > (214/2) and dist < (324/2):
        zone = 3
    elif dist > (324/2) and dist < (340/2):
        zone = 5
    else:
        zone = 6

    deg = math.degrees(math.atan2(y, x))

    num = 0

    if deg > (-9) and deg < 9:
        num = 6
    elif deg > 9 and deg < 27:
        num = 13
    elif deg > 27 and deg < 45:
        num = 4
    elif deg > 45 and deg < 63:
       num =18
    elif deg > 63 and deg < 81:
       num = 1
    elif deg > 81 and deg < 99:
       num = 20
    elif deg > 99 and deg < 117:
       num = 5
    elif deg > 117 and deg < 135:
       num = 12
    elif deg > 135 and deg < 153:
       num = 9
    elif deg > 153 and deg < 171:
       num = 14
    elif deg > 171 or deg < -171:
       num = 11
    elif deg < -9 and deg > -27:
        num = 10
    elif deg < -27 and deg > -45:
        num = 15
    elif deg < -45 and deg > -63:
       num =2
    elif deg < -63 and deg > -81:
       num = 17
    elif deg < -81 and deg > -99:
       num = 3
    elif deg < -99 and deg > -117:
       num = 19
    elif deg < -117 and deg > -135:
       num = 7
    elif deg < -135 and deg > -153:
       num = 16
    elif deg < -153 and deg > -171:
       num = 8

    score = ''

    if zone == 1:
        score = 'DB'
    elif zone == 2:
        score = 'SB'
    elif zone == 3:
        score = str(num)
    elif zone == 4:
        score = 'T' + str(num)
    elif zone == 5:
        score = 'D' + str(num)
    elif zone == 6:
         score = 'X'

    return score
