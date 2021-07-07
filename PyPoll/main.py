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

    line1 = ("\nElection Results")
    line2 = ("--------------------")
    line3 = ("Total Votes: " + str(count))
    line4 = ("--------------------")

    print (line1)
    print(line2)
    print(line3)
    print(line4)

    max_vote = 0
    print_list =[]
    while cand_count2 < cand_count:
        for x in candidate_row:
            if x == cand_list[cand_count2]:
                vote_count = vote_count + 1
        if vote_count > max_vote:
            winner = cand_list[cand_count2]
            max_vote = vote_count
        percent = "{:.2%}".format(vote_count / count)
        cand_type = (cand_list[cand_count2] + ": " + str(percent) + " (" + str(vote_count) + ")")
        print_list.append(cand_type)
        vote_count = 0      
        cand_count2 = cand_count2 + 1
    
    print_count = 0
    line5 = ("--------------------")
    line6 = ("Winner: " + str(winner))
    line7 = ("--------------------")
    while print_count < len(print_list):
        print(print_list[print_count])
        print_count = print_count + 1
    print(line5)
    print(line6)
    print(line7)  

print_count = 0
output_file = os.path.join('analysis','output.txt')

with open(output_file, 'a') as out:
    out.write(line1 + '\n')
    out.write(line2 + '\n')
    out.write(line3 + '\n')
    out.write(line4 + '\n')
    while print_count < len(print_list):
        out.write(print_list[print_count] + '\n')
        print_count = print_count+1
    out.write(line5 + '\n')
    out.write(line6 + '\n')
    out.write(line7 + '\n')