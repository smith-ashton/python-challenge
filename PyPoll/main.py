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
    for row in csvreader:
        candidate_row.append(row[2])
        count = count + 1

    for x in candidate_row:
        if x not in cand_list:
            cand_list.append(x)
    print(cand_list)   


            



#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.