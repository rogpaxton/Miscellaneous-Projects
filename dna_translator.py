def translate_with_frame(dna, frames=[1,2,3,-1,-2,-3]):

    codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }

    bases = list(dna)
    bases_rvs = bases.reverse()

    frame1 = []
    frame2 = []
    frame3 = []
    frame_1 = []
    frame_2 = []
    frame_3 = []

    iter = 0
    sub_list1 = []
    sub_list_1 = []
    sub_list2 = []
    sub_list_2 = []
    sub_list3 = []
    sub_list_3 = []

    iter = 0
    adder1 = ''
    adder2 = ''
    adder3 = ''
    adder_1 = ''
    adder_2 = ''
    adder_3 = ''

    for i in bases:
        sub_list1.append(i)
        if i == "A":
            sub_list_1.append("T")
        if i == "T":
            sub_list_1.append("A")
        if i == "G":
            sub_list_1.append("C")
        if i == "C":
            sub_list_1.append("G")
        iter += 1
        if iter == 3:
            iter = 0
            adder1 = ''.join(sub_list1)
            frame1.append(adder1)
            sub_list_1.reverse()
            adder_1  = ''.join(sub_list_1)
            frame_1.append(adder_1)
            sub_list1 = []
            sub_list_1 = []
    if len(adder_1) < 3:
        frame_1.append(adder_1)

    frame_1.reverse()
    frame_1_compile = []
    final_frame_1 = []

    for i in frame_1:
        breaker_1 = list(i)
        for j in breaker_1:
            frame_1_compile.append(j)
    sub_list_1 = []
    iter = 0
    adder_1 = []
    for i in frame_1_compile:
        sub_list_1.append(i)
        iter += 1
        if iter == 3:
            iter = 0
            adder_1  = ''.join(sub_list_1)
            final_frame_1.append(adder_1)
            sub_list_1 = []


    del bases[0]
    print frame1
    print frame_1

    iter = 0

    for i in bases:
        sub_list2.append(i)
        if i == "A":
            sub_list_2.append("T")
        if i == "T":
            sub_list_2.append("A")
        if i == "G":
            sub_list_2.append("C")
        if i == "C":
            sub_list_2.append("G")
        iter += 1
        if iter == 3:
            iter = 0
            adder2 = ''.join(sub_list2)
            frame2.append(adder2)
            sub_list_2.reverse()
            adder_2  = ''.join(sub_list_2)
            frame_2.append(adder_2)
            sub_list2 = []
            sub_list_2 = []

    if len(adder_2) < 3:
        frame_1.append(adder_2)

    frame_2.reverse()
    frame_2_compile = []
    final_frame_2 = []

    for i in frame_2:
        breaker_2 = list(i)
        for j in breaker_2:
            frame_2_compile.append(j)
    sub_list_2 = []
    iter = 0
    adder_2 = []
    for i in frame_2_compile:
        sub_list_2.append(i)
        iter += 1
        if iter == 3:
            iter = 0
            adder_2  = ''.join(sub_list_2)
            final_frame_2.append(adder_2)
            sub_list_2 = []


    del bases [0]

    iter = 0

    for i in bases:
        sub_list3.append(i)
        if i == "A":
            sub_list_3.append("T")
        if i == "T":
            sub_list_3.append("A")
        if i == "G":
            sub_list_3.append("C")
        if i == "C":
            sub_list_3.append("G")
        iter += 1
        if iter == 3:
            iter = 0
            adder3 = ''.join(sub_list3)
            frame3.append(adder3)
            sub_list_3.reverse()
            adder_3  = ''.join(sub_list_3)
            frame_3.append(adder_3)
            sub_list3 = []
            sub_list_3 = []

    if len(adder_3) < 3:
        frame_3.append(adder_3)

    frame_3.reverse()
    print frame_3
    frame_3_compile = []
    final_frame_3 = []

    for i in frame_3:
        breaker_3 = list(i)
        for j in breaker_3:
            frame_3_compile.append(j)
    sub_list_3 = []
    iter = 0
    adder_3 = []
    for i in frame_3_compile:
        sub_list_3.append(i)
        iter += 1
        if iter == 3:
            iter = 0
            adder_3  = ''.join(sub_list_3)
            final_frame_3.append(adder_3)
            sub_list_3 = []


    frame1_AA = []
    frame2_AA = []
    frame3_AA = []
    frame_1_AA = []
    frame_2_AA = []
    frame_3_AA = []

    for i in frame1:
        if i in codontable:
            frame1_AA.append(codontable[i])
        else:
            frame1_AA.append('*')

    for i in frame2:
        if i in codontable:
            frame2_AA.append(codontable[i])
        else:
            frame2_AA.append('*')

    for i in frame3:
        if i in codontable:
            frame3_AA.append(codontable[i])
        else:
            frame3_AA.append('*')

    for i in final_frame_1:
        if i in codontable:
            frame_1_AA.append(codontable[i])
        else:
            frame_1_AA.append('*')

    for i in final_frame_2:
        if i in codontable:
            frame_2_AA.append(codontable[i])
        else:
            frame_2_AA.append('*')

    for i in final_frame_3:
        if i in codontable:
            frame_3_AA.append(codontable[i])
        else:
            frame_3_AA.append('*')

    frame1_AA_op = ''.join(frame1_AA)
    frame2_AA_op = ''.join(frame2_AA)
    frame3_AA_op = ''.join(frame3_AA)
    frame_1_AA_op = ''.join(frame_1_AA)
    frame_2_AA_op = ''.join(frame_2_AA)
    frame_3_AA_op = ''.join(frame_3_AA)

    AA_op = []

    for i in frames:
        if i == 1:
            AA_op.append(str(frame1_AA_op))
        elif i == 2:
            AA_op.append(str(frame2_AA_op))
        elif i == 3:
            AA_op.append(str(frame3_AA_op))
        elif i == -1:
            AA_op.append(str(frame_1_AA_op))
        elif i == -2:
            AA_op.append(str(frame_2_AA_op))
        elif i == -3:
            AA_op.append(str(frame_3_AA_op))

    return AA_op


    #your code here - use the preloaded dict codons for conversions
