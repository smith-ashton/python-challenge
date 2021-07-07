#imports
import os
import csv

#read csv
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

#GETTING LIST OF CANDIDATES
# set up variables
    #creating list out of csv candidate row to count and count for for loop
    candidate_row = []
    count = 0
    #creating list to get unique candidates and do each of the counts later and count for for loop
    cand_list = []
    cand_count = 0

#put all data in candidate row into a list
    for row in csvreader:
        candidate_row.append(row[2])
        count = count + 1
#sorting through csv to get unique names and total votes
    for x in candidate_row:
        if x not in cand_list:
            cand_list.append(x)
            cand_count = cand_count + 1

#set up first part of printed lines
    line1 = ("\nElection Results")
    line2 = ("--------------------")
    line3 = ("Total Votes: " + str(count))
    line4 = ("--------------------")
#print header and count
    print (line1)
    print(line2)
    print(line3)
    print(line4)

#GET VOTE COUNT FOR EACH CANDIDATE
#set up variables
    #use to keep track of number of votes for each candidate
    vote_count = 0
    #use to keep track of which candidate you are searching for (index)
    cand_count2 = 0
    #use to keep track of the row with the highest number of votes
    max_vote = 0
    #set up list of final info for each candidate to print later
    print_list =[]

    #loop through list of all candidates
    while cand_count2 < cand_count:
        #loop through list of all votes cast
        for x in candidate_row:
            #if the row is the same as the candidate you are searching for, add to vote count
            if x == cand_list[cand_count2]:
                vote_count = vote_count + 1

        #finding winner - after counts are totaled, if count is greater than current greatest, replace winner
        if vote_count > max_vote:
            winner = cand_list[cand_count2]
            max_vote = vote_count

        #calcluate percentage of votes for each candidate and format
        percent = "{:.2%}".format(vote_count / count)

        #set line of text for each candidate
        cand_type = (cand_list[cand_count2] + ": " + str(percent) + " (" + str(vote_count) + ")")
        #add line of text to list for printing
        print_list.append(cand_type)

        #reset vote count for next candidate
        vote_count = 0      

        cand_count2 = cand_count2 + 1
    
    #set count for print loop
    print_count = 0
    #set up lines to print 
    line5 = ("--------------------")
    line6 = ("Winner: " + str(winner))
    line7 = ("--------------------")

    #loop through each candidate and print the info in list
    while print_count < len(print_list):
        print(print_list[print_count])
        print_count = print_count + 1
    #print rest of information
    print(line5)
    print(line6)
    print(line7)  
    
#EXPORTING
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