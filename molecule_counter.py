def parse_molecule (formula):

    form_list = list(formula)

    for index, i in enumerate(form_list):
        if i.isdigit():
            form_list[index] = int(i)

    for index, i in enumerate(form_list):
        if isinstance(i, str) and i.islower():
            form_list[index] = form_list[index - 1] + i
            form_list[index - 1] = '*'

    if '*' in form_list:
        form_list.remove('*')

    print form_list

    form_list.reverse()

    mol_dict = {i:1 for i in form_list if isinstance(i,str) and i != '(' and i != ')'and i != '['and i != ']'}

    for index, i in enumerate(form_list):
        if isinstance(i, int) and form_list[index+1] in mol_dict:
            mol_dict[str(form_list[index+1])] *= i

    print mol_dict
    return mol_dict
