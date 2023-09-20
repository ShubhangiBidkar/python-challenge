import os
import csv


# Define PyBank's variables
months = []
profit_loss_changes = []


total_months= 0
net_profit_loss=0
current_month_profit_loss=0
previous_month_profit_loss=0
profit_loss_change=0



# Path to collect data from the Resources folder
budget_csv =os.path.join("Resources", "budget_data.csv")

# Open and read the csv file
with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")

   

 # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
   
   

 # Read each row of data after the header
    for row in csvreader:
        # Count of months
        total_months +=1

         # Net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss +=int(row[1])
        net_profit_loss +=current_month_profit_loss

        if(total_months == 1):
              # Make the value of previous month to be equal to current month
              previous_month_profit_loss = current_month_profit_loss
        else:
             # Compute change in profit loss
            profit_loss_change= current_month_profit_loss - previous_month_profit_loss      

            # Append each month to the months[]
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

             #sum and average of the changes in "Profit/Losses" over the entire period
            sum_profit_loss = sum(profit_loss_changes)
            average_profit_loss = round(sum_profit_loss/(total_months - 1), 2)

             # highest and lowest changes in "Profit/Losses" over the entire period
            highest_change = max(profit_loss_changes)
            lowest_change = min(profit_loss_changes)

            # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
            highest_month_index = profit_loss_changes.index(highest_change)
            lowest_month_index = profit_loss_changes.index(lowest_change)

            # Assign best and worst month
            best_month = months[highest_month_index]
            worst_month = months[lowest_month_index]


# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

# -->>  Export a text file with the results
budget_file = os.path.join("Analysis", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {total_months}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")