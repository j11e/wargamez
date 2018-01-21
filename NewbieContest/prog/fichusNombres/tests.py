first_answer = ['', 0, 0]

year = 5
men_count = 5
women_count = 7
total = 12 # for convenience
abductions = ["H", "F", "HF", "FHF", "HFFHF"]

stop = False
while not stop:
    year += 1
    print("Year %d; total: %d" % (year, men_count + women_count))

    # calculate this year's abductions
    abductions.append(abductions[-2] + abductions[-1])
    abductions = abductions[1:] # to avoid increasing in size too much

    # "perform" the abductions and look for answers to the 1st question
    for gender in abductions[-1]:
        total += 1

        if gender == "H":
            men_count += 1
        else:
            women_count += 1

        if total == 1000000000:
            first_answer[0] = gender
            first_answer[1] = men_count
            first_answer[2] = women_count
    
        if first_answer[0] != "":
            stop = True

print("answers: %s %d %d" % (first_answer[0], first_answer[1], first_answer[2]))

