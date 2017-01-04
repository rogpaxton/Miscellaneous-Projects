def processes(start, end, processes):

    print start
    print end
    print processes

    proc = []
#    target = ''
    iter = 0

    if start == '' or end == '' or processes == [] :
        return proc

    flattended_processes = [item for sublist in processes for item in sublist]

    if start not in flattended_processes:
        return proc
    if end not in flattended_processes:
        return proc

    if start == end:
        return proc


    while iter < len(processes)+1:
        for i in processes:
            if start == i[1]:
                proc.append(i[0])
                target = i[2]
            if target == end:
                print proc
                return proc
                break
            else:
                start = target
                iter += 1

    return proc
            
