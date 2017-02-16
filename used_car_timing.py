def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    month = 0
    savings = 0
    old = float(startPriceOld)
    new = float(startPriceNew)
    difference = 0.0
    loss = percentLossByMonth

    if (savings + old) > new:
        return [0, int(savings + old - new)]

    while new > (old + savings):
        month += 1
        savings += savingperMonth
        if month % 2 == 0:
            loss += 0.5
        old -= old * (loss/100)
        new -= new * (loss/100)
        difference = savings + old - new

    return [month, int(difference)]
