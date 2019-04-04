import os
import csv
#Creating a path for the budget data
bankbudget = os.path.join("budget_data.csv")
# Open csv file
with open(bankbudget, 'r') as csvfile:
#Split the csv file
    readCSV = csv.reader(csvfile, delimiter=',')

    #Read header first
    csv_header= next(readCSV)

    #Get the number of months 
    row_count = sum(1 for row in readCSV)
    csvfile.seek(0)
    next(readCSV)

    print ("Financial Analysis")
    print ("------------------------------")
    print (f"Total Months : {row_count}")



    # Assigning values at 0 so that 
    totalmonths = 0
    totalvalue = 0
    averagePL = []
    highPL = 0
    lowPL = 0
    sum_profit = 0

    lowdate = ''
    highdate = ''
# In my four loop the white line goes from for row down to total value because thats what Ive specified
# as a scope. The reason I have loops is to test the same code and test it on multiple numbers/objects
# Whatever is in scope gets called for all different objects.
    for row in readCSV:
        profit = int(row[1])
        totalvalue = totalvalue + profit
        averagePL = averagePL +[profit]
# We need to find the highest profit and lowest. Max is a function to give us the highest. Put it towards averagePL and you will
#get the greatest profit. Same with the lowest
        if(int(row[1]) == max(averagePL)):
            highPL = max(averagePL)
            highdate = row[0]

        if(int(row[1]) == min(averagePL)):
            lowPL = min(averagePL)
            lowdate = row[0]

    print(f"Total: {totalvalue}")
    print(f"Average Change: {sum(averagePL)/len(averagePL)}")



#Do all the writing and printing.....n????
f = open("budget_results.txt", "w")
f.write("Budget Info\n")
#Greatest increase of profits (current month total - previous total)
print ("Highest Increase  " + highdate + "  " + str(highPL))
f.write("Highest Increase  " + highdate + "  " + str(highPL)+" \n") 
print("Highest Decrease  " + lowdate + "  " + str(lowPL))
f.write ("Highest Decrease  " + lowdate  + "  " + str(lowPL)+" \n")










