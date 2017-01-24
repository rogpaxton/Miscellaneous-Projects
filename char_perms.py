def is_valid_coordinates(coordinates):

    import re
    num_format = re.compile(r'^\-?[0-9][0-9]*\.?[0-9]*')

    op = True

    coords = coordinates.split(', ')

    for i in coords:
        decimal_counter = 0
        dash_counter = 0
        ind_lst = list(i)
        for index, j in enumerate(ind_lst):
            if j == '-' and index > 0:
                return False
            if j == '.':
                decimal_counter += 1
            if decimal_counter > 1:
                return False
            if j == '-':
                dash_counter += 1
            if dash_counter > 1:
                return False
            if j == ',':
                return False
            if j not in ['-', '.', 'N', 'S', 'E', 'W', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return False

    coords_float = []
    for i in coords:
#        if isinstance(i, float) or isinstance(i, int):
#        if i.isdigit():
#            coords_float.append(float(i))
        isnumber = re.match(num_format,i)
        if isnumber:
            coords_float.append(float(i))
        else:
            return False

    if coords_float[0] < -90 or coords_float[0] > 90:
        return False

    if coords_float[1] < -180 or coords_float[0] > 180:
        return False

    return op
