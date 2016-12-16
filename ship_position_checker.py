def validateBattlefield(field):

#correct soln; 4 @ 1, 3 @ 2, 2 @ 3, 1 @ 4, 0 > 4
    correct = [4, 3, 2, 1, 0]
    soln = [0, 0, 0, 0, 0]

    adder = 0
    x = 0
    y = 0

    for index, i in battlefield:
        for j in i:
            if j == 1 and enumerate[j] <= 9:


#across

#down

#check if diagonal; adjacent will show as incorrect soln automatically

    if soln == correct:
        return True
    else:
        return False
	return True;
