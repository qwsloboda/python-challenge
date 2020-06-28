import os
import csv

csvpath = os.path.join( 'python-challenge' ,'PyBank' ,'Resources', 'budget_data.csv')

print("opening", csvpath)
months = []
prolos = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    print(csvreader)
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        #print("month", row[0], "Profit/Losses", row[1])
        months.append(row[0])
        prolos.append(row[1])
        #months_sum = 0
        #months = months_sum(sum(months))
        
        net_total = 0
        for item in prolos:
            net_total = net_total + int(item)
            first_num = int(prolos[0])
            final_num = int(prolos[len(prolos)-1])
            avg_change = (final_num - first_num) / 85
        profit_changes = []
        for i in range(len(prolos)-1):
            profit_changes.append(int(int(prolos[i+1])-int(prolos[i])))
            i = i+1
            max_profit = max(profit_changes)
            min_profit = min(profit_changes)
            max_profit_index = profit_changes.index(max(profit_changes))
            min_profit_index = profit_changes.index(min(profit_changes))
    
    max_month = months[max_profit_index + 1]        
    min_month = months[min_profit_index +1]

    print("Total Months: " + str(len(months)))
    print("Total: $" + str(net_total))
    print("Average Change: $" + str(avg_change))
    print("Greatest Increase in Profits: " + max_month + " ($" + str(max_profit) + ")")
    print("Greatest Decrease in Profits: " + min_month + " ($" + str(min_profit) + ")")
    #print(max_profit)
    #print(min_profit)
    #print(max_profit_index)    
    #print(min_profit_index)
    
    
      
        


    
    
