def stat(strg):

    import re
    from numpy import median

    strg_list = strg.split()
    new_strg_list = []

    for i in strg_list:
        new = re.sub(',', '', i)
        new_strg_list.append(new)

    conv_sec_list = []

    for j in new_strg_list:
        new = j.split('|')
        secs = 0
        secs += int(new[0]) * 3600
        secs += int(new[1]) * 60
        secs += int(new[2])

        conv_sec_list.append(secs)

    ranger = max(conv_sec_list) - min(conv_sec_list)
    ranger_hour = ranger / 3600
    ranger_min = (ranger - (ranger_hour*3600)) / 60
    ranger_sec = ranger - (ranger_hour * 3600) - (ranger_min * 60)
    ranger_str = str(ranger_hour).zfill(2) + '|' + str(ranger_min).zfill(2) + '|' + str(ranger_sec).zfill(2)

    averager = reduce(lambda x, y: x + y, conv_sec_list) / len(conv_sec_list)
    averager_hour = averager / 3600
    averager_min = (averager - (averager_hour*3600)) / 60
    averager_sec = averager - (averager_hour * 3600) - (averager_min * 60)
    averager_str = str(averager_hour).zfill(2) + '|' + str(averager_min).zfill(2) + '|' + str(averager_sec).zfill(2)

    medianer = int(median(conv_sec_list))
    medianer_hour = medianer / 3600
    medianer_min = (medianer - (medianer_hour*3600)) / 60
    medianer_sec = medianer - (medianer_hour * 3600) - (medianer_min * 60)
    medianer_str = str(medianer_hour).zfill(2) + '|' + str(medianer_min).zfill(2) + '|' + str(medianer_sec).zfill(2)

    results = "Range: " + ranger_str + " Average: " + averager_str + " Median: " + medianer_str

    return results
