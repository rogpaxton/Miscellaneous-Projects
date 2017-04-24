def count_if(values,criteria):

    count = 0
    if type(criteria) is str:
        crit_list = list(criteria)
    if type(criteria) is int or type(criteria) is float:
        for i in values:
            if i == criteria:
                count += 1
    elif '<' not in crit_list and '>' not in crit_list and '=' not in crit_list:
        for i in values:
            if i == criteria:
                count += 1
    else:
        num_list = []
        for i in crit_list:
            if i.isdigit() or i == '.':
                num_list.append(i)
        if '.' in num_list:
            num = float(''.join(num_list))
        else:
            num = int(''.join(num_list))
        if '<' not in crit_list and '>' not in crit_list and '=' not in crit_list:
            for i in values:
                if i == criteria:
                    count += 1
        elif '>' in crit_list and '=' in crit_list:
            for i in values:
                if i >= num:
                    i
                    count += 1
        elif '<' in crit_list and '=' in crit_list:
            for i in values:
                if i <= num:
                    count += 1
        elif '<' in crit_list and '>' in crit_list:
            for i in values:
                if i != num:
                    count += 1
        elif '=' in crit_list:
            for i in values:
                if i == num:
                    count += 1
        elif '>' in crit_list:
            for i in values:
                if i > num:
                    count += 1
        elif '<' in crit_list:
            for i in values:
                if i < num:
                    count += 1

    return count

def sum_if(values,criteria):

    sum = 0
    if type(criteria) is str:
        crit_list = list(criteria)
    if type(criteria) is int or type(criteria) is float:
        for i in values:
            if i == criteria:
                sum += i
    elif '<' not in crit_list and '>' not in crit_list and '=' not in crit_list:
        for i in values:
            if i == criteria:
                sum += i
    else:
        num_list = []
        for i in crit_list:
            if i.isdigit() or i == '.':
                num_list.append(i)
        if '.' in num_list:
            num = float(''.join(num_list))
        else:
            num = int(''.join(num_list))
        if '<' not in crit_list and '>' not in crit_list and '=' not in crit_list:
            for i in values:
                if i == criteria:
                    sum += i
        elif '>' in crit_list and '=' in crit_list:
            for i in values:
                if i >= num:
                    sum += i
        elif '<' in crit_list and '=' in crit_list:
            for i in values:
                if i <= num:
                    sum += i
        elif '<' in crit_list and '>' in crit_list:
            for i in values:
                if i != num:
                    sum += i
        elif '=' in crit_list:
            for i in values:
                if i == num:
                    sum += i
        elif '>' in crit_list:
            for i in values:
                if i > num:
                    sum += i
        elif '<' in crit_list:
            for i in values:
                if i < num:
                    sum += i

    return sum

def average_if(values,criteria):

    sum = 0
    count = 0
    if type(criteria) is str:
        crit_list = list(criteria)
    if type(criteria) is int or type(criteria) is float:
        for i in values:
            if i == criteria:
                sum += i
                count += 1
    elif '<' not in crit_list and '>' not in crit_list and '=' not in crit_list:
        for i in values:
            if i == criteria:
                sum += i
                count += 1
    else:
        num_list = []
        for i in crit_list:
            if i.isdigit() or i == '.':
                num_list.append(i)
        if '.' in num_list:
            num = float(''.join(num_list))
        else:
            num = int(''.join(num_list))
        if '<' not in crit_list and '>' not in crit_list and '=' not in crit_list:
            for i in values:
                if i == criteria:
                    sum += i
                    count += 1
        elif '>' in crit_list and '=' in crit_list:
            for i in values:
                if i >= num:
                    sum += i
                    count += 1
        elif '<' in crit_list and '=' in crit_list:
            for i in values:
                if i <= num:
                    sum += i
                    count += 1
        elif '<' in crit_list and '>' in crit_list:
            for i in values:
                if i != num:
                    sum += i
                    count += 1
        elif '=' in crit_list:
            for i in values:
                if i == num:
                    sum += i
                    count += 1
        elif '>' in crit_list:
            for i in values:
                if i > num:
                    sum += i
                    count += 1
        elif '<' in crit_list:
            for i in values:
                if i < num:
                    sum += i
                    count += 1

    return float(sum) / float(count)
