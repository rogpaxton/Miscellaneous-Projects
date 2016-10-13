def hollow_triangle(n):

    lines = []
    linestr = ''

    #intial row
    for i in range (n-1):
        linestr += '_'
    linestr += '#'
    for i in range (n-1):
        linestr += '_'
    lines.append(linestr)

    #body rows

    for i in range(n-2):
        linestr = ''
        #_
        for j in range(n - i-2):
            linestr += '_'
        ##
        linestr += '#'
        #_
        for k in range(i+1):
            linestr += '_'
            if k > 0:
                linestr += '_'
        ##
        linestr += '#'
        #_
        for j in range(n - i-2):
            linestr += '_'
        #append to list
        lines.append(linestr)

    #final row
    linestr = ''
    for i in range(len(lines[0])):
        linestr += '#'
    lines.append(linestr)

    return lines
