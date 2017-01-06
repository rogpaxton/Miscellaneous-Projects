def runoff(voters):

    from collections import Counter
    import operator
    from collections import defaultdict
#    from collections import iteritems

    print voters

    decision = 0

    while decision == 0:
        votes = len(voters)
        empties = 0
        for i in voters:
            if i == []:
                empties +=1
        if empties == votes:
            return None
        init_list = [i[0] for i in voters]

        init_votes = Counter(init_list)
        votes_dict = dict(init_votes)
        greatest = max(votes_dict, key=votes_dict.get)
        same_vals = defaultdict(list)
        for k, v in votes_dict.iteritems():
            same_vals[v].append(k)
        lowest_group = same_vals.get(min(same_vals))

#        not in votes
        not_in_votes = []
        for i in voters[0]:
            if i not in init_list:
                not_in_votes.append(i)

        if votes_dict[greatest] > votes/2:
            decision = 1
            winner = max(init_votes.iteritems(), key=operator.itemgetter(1))[0]
            op = str(winner)
        elif not_in_votes != []:
            for i in not_in_votes:
                for j in voters:
                    j.remove(i)
        elif len(lowest_group) > 1:
            for i in lowest_group:
                for j in voters:
                    j.remove(i)
        else:
            least = min(votes_dict, key=votes_dict.get)
            for i in voters:
                i.remove(least)


    return op





        
