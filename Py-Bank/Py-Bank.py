import os
import csv

#csv file path
csvpath = os.path.join("C:/Users/steel/GT-ATL-DATA-PT-12-2019-U-C/Homework/03-Python/Instructions/PyBank/Resources","budget_data.csv")

#creating lists
profit_losses = []
months = []
ch = []

#open csv & header
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    csvheader = next(csvreader)
    #initialize values
    Total = 0
    Total4 = 0
    Average = 0
    for row in csvreader: 

        #cast starting values of variables
        Total2 = 0
         #split profit/loss and months into two seperate lists
        profit_losses.append(row[1])
        months.append(row[0])       
        #list for changes
        ch = [int(profit_losses[i+1])-int(profit_losses[i]) for i in range(len(profit_losses)-1)]
        #Summing total
        Total += int(row[1])

    #sum of Change list  
    Total4 = sum(ch)

    #greatest increase
    large= max(ch)
    #calling index for large value (adding +1 to accound for less values in change list)
    datelarge=months[ch.index(large)+1]
    
            #greatest decrease
    small= min(ch)
    #calling index for small value (adding +1 to accound for less values in change list)
    datesmall=months[ch.index(small)+1]
    
    #Average Change    
    Average = round(Total4/len(ch),2)
   

    #total months
    Total2 = len(months) 
    

            #print values 
    print (str("Financial Analysis"))
    print (str("----------------------------------"))
    print (str("Total Months: ") + str(Total2))
    print (str("Total: ") + str(Total))
    print (str("Average Change: ") + str(Average))
    print (str("Greatest Decrease in Profits: ") + str(datesmall) + (str(" ")) + str("(") + str(small) + str(")"))
    print (str("Greatest Increase in Profits: ") + str(datelarge) + (str(" ")) + str("(") + str(large) + str(")"))
   
       
with open('Py-Bank/pybankresults.txt', 'w') as f:
    f.write(str("Financial Analysis")+'\n')
    f.write(str("----------------------------------")+'\n')
    f.write(str("Total Months: ") + str(Total2)+'\n')
    f.write(str("Total: ") + str(Total)+'\n')
    f.write(str("Average Change: ") + str(Average)+'\n')
    f.write(str("Greatest Decrease in Profits: ") + str(datesmall) + (str(" ")) + str("(") + str(small) + str(")")+'\n')
    f.write(str("Greatest Increase in Profits: ") + str(datelarge) + (str(" ")) + str("(") + str(large) + str(")")+'\n')
f.close