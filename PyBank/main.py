#imports
import os
import csv

#read csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    count = 0
    total = 0
    greatest = 0
    least = 0
    for row in csvreader:
#Calculate total number on months included in the dataset
        count = count + 1
#Calculate net total amount of "Profit/Losses" over the entire period
        total = total + float(row[1])
#Calculate greatest increase in profits (date and amount) over the entire period
        if float(row[1]) > greatest:
            greatest = float(row[1])
            greatest_month = row[0]
#Calculate greatest decrease in losses (date and amount) over the entire period
        if float(row[1]) < least:
            least = float(row[1])
            least_month = row[0]
    average = total / count
#set up print
    line1 = ("\nFinancial Analysis")
    line2 = ("----------------------")
    line3 = ("Total Months: " + str(count))
    line4 = ("Total: $" + str(total))
    line5 = ("Average Change: $" + str(round(average,2)))
    line6 = ("Greatest Increase in Profits: " + greatest_month + "($" + str(greatest) + ")")
    line7 = ("Greatest Decrease in Profits: " + least_month + "($" + str(least) + ")\n")
    
#Print to terminal
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)

#Print to text file
output_file = os.path.join('analysis','output.txt')

with open(output_file, 'a') as out:
    out.write(line1 + '\n')
    out.write(line2 + '\n')
    out.write(line3 + '\n')
    out.write(line4 + '\n')
    out.write(line5 + '\n')
    out.write(line6 + '\n')
    out.write(line7 + '\n')