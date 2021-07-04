import os
import csv

#read csv
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    candidate_row = []
    count = 0
    cand_list = []
    vote_count = 0
    cand_count = 0
    cand_count2 = 0
#sorting through csv to get unique names and total votes
    for row in csvreader:
        candidate_row.append(row[2])
        count = count + 1

    for x in candidate_row:
        if x not in cand_list:
            cand_list.append(x)
            cand_count = cand_count + 1

    print ("\nElection Results")
    print("--------------------")
    print("Total Votes: " + str(count))
    print("--------------------")

    while cand_count2 < cand_count:
        for x in candidate_row:
            if x == cand_list[cand_count2]:
                vote_count = vote_count + 1
        percent = "{:.2%}".format(vote_count / count)
        print (cand_list[cand_count2] + ": " + str(percent) + "% (" + str(vote_count) + ")")
        vote_count = 0
        cand_count2 = cand_count2 + 1
    