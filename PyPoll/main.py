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

    for row in csvreader:
        candidate_row.append(row[2])
        count = count + 1

    for x in candidate_row:
        if x not in cand_list:
            cand_list.append(x)
            cand_count = cand_count + 1

    while cand_count2 < cand_count:
        for x in candidate_row:
            if x == cand_list[cand_count2]:
                vote_count = vote_count + 1
        print (cand_list[cand_count2], vote_count)
        cand_count2 = cand_count2 + 1


#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.