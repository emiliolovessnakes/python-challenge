#Import your dependendies 
import csv 
import os

#Specify the paths of your csv file and text file ,
input_file = os.path.join("PyBank", "Resources", "budget_data.csv") # This is where the system goes to read and analyzee te he data (from the csv file)
output_file = os.path.join("PyBank", "Resources", "budgetanalysis.txt") #This is where the system goes to actually write out a summary of data that it collected from the csv file '

#Initialize your variables 
counter_total_months = 0 
monthly_change = [] #Create a variable that will store each month in an empty list
net_change_list = [] #Create a variable that will store each net change in an empty list
greatest_increase = ["",0]
greatest_decrease = ["",99999999999]
counter_net_total = 0

#Open the csv file and begin your analysis 
with open(input_file) as financial_data:
    reader = csv.reader(financial_data) #Create a variable that reads teh csv file
    skip_header = next(reader) #Create a variable that skips the header aka the first row of the reader which contains the csv file promptly called "financial_data"
    header = next(reader) # Create a variable that reads the first row of the csv file
    first_row = next(reader) # Create a variable that store and extracts the first row of the csv file so that the program will start on teh second row 
    counter_total_months +=  1 #Recursively iterate the total months counter so that it adds one to itself 
    counter_net_total += int(first_row[1]) #Initialize net total counter
    net_previous = int(first_row[1]) #Initialize variable and holds teh very first value of the profit/loss column that is actually an integer and not a part of the header

    # Create a loop that iterate across each and every row of the csv file 
    for row in reader:
        
        counter_total_months += 1 #Recrusion 
        counter_net_total += int(row[1]) #Still recursion but of a particular column (column 2 where the profits/osses are stored)

        net_change = int(row[1]) - net_previous #Simple subtraction between teh second value and first value of the second column
        net_previous = int(row[1]) # Create a variable that stores what the previous net value was
        net_change_list += [net_change] #Create a variable that recursively calculuate, applies and stores the base net change rate in a lst
        monthly_change += [row[0]] #Create a variable that recursively stores each month in a list
        
        if net_change > greatest_increase[1]:
             greatest_increase[0] = row[0] #greatest_increase[0] is the month that experienced the greatest increase in profit
             greatest_increase[1] = net_change #greatest_increase[1] is the actual integer value that has the greater among among the entire second column
        
        if net_change < greatest_decrease[1]:
             greatest_decrease[0] = row[0]
             greatest_decrease[1] = net_change
             
# Calculate the average net change for each month
# The function len stands for length and it finds the length of the net change list
average_net_change = sum(net_change_list) / len(net_change_list)

# Output your analysis
output = (
     f"Financial Analysis\n"
     f"------------------------------"
     f"Total Months: {counter_total_months}\n"
     f"Total: ${counter_net_total}\n"
     f"Average Change: ${average_net_change:.2f}\n"
     f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
     f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(output)

#Send the summary of your results to the text file
with open(output_file, "w") as textfile:
     textfile.write(output)

