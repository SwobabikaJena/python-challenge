import os
import csv

budgetdata_path = os.path.join('Resources', 'budget_data.csv')

with open(budgetdata_path, newline='') as budgetdata_file: 
    budgetdata_reader= csv.reader(budgetdata_file, delimiter=",")
    

    exclude_header = next(budgetdata_file)

    values = []
    months = []
    total_months = 0
    total_profitloss = 0

    # For Total months and Total profit over the entire period:
    for row in budgetdata_reader:
        total_months = total_months + 1
        total_profitloss = total_profitloss + int(row[1])
        values.append(row[1])
        months.append(row[0]) 
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months} ")  
    print(f"Total: ${total_profitloss}")  
    months.pop(0)
    

    # For Average change over the entire period:

    initial_value = values[0]
    final_value = values[len(values)-1]
    avg_change = float((int(final_value) - int(initial_value))/(total_months-1)) 
    
    print(f"Average Change: ${round(avg_change,2)}")

    # For greatest increase and decrease in Profit/Losses over the entire period:
    diff_amount = []
    length = len(values)

    for x in range(1,length):
        difference = int(values[x]) - int(values[x-1])
        diff_amount.append(difference)
   

    max_diff_index = diff_amount.index(max(diff_amount))
    print (f"Greatest Increase in Profits: {months[max_diff_index]} (${max(diff_amount)})")
    
    min_diff_index = diff_amount.index(min(diff_amount))
    print (f"Greatest Decrease in Profits: {months[min_diff_index]} (${min(diff_amount)})")

    # To create an output text file with the results:
    outfile = 'Analysis/output.txt'
    with open(outfile,'w') as text:
        lines = text.write("Financial Analysis \n")
        lines = text.write("---------------------------- \n")
        lines = text.write(f"Total Months: {total_months}\n") 
        lines = text.write(f"Total: ${total_profitloss} \n") 
        lines = text.write(f"Average Change: ${round(avg_change,2)}\n") 
        lines = text.write(f"Greatest Increase in Profits: {months[max_diff_index]} (${max(diff_amount)})\n") 
        lines = text.write(f"Greatest Decrease in Profits: {months[min_diff_index]} (${min(diff_amount)})") 
    




    

    
  
  
    
   
    

   
