def basic_op(op, value1, value2):
    import operator

    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}

    return ops[op](value1,value2)
