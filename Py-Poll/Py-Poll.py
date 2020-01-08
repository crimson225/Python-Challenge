import os
import csv
candidates = []
unique_candidates = []
csvpath = os.path.join("C:/Users/steel/GT-ATL-DATA-PT-12-2019-U-C/Homework/03-Python/Instructions/PyPoll/Resources","election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    csvheader = next(csvreader)
    #seperate candidates into seperate row
    for row in csvreader:
        candidates.append(row[2])
        
    #gathering unique names of candidates into seperate list.
    for item in candidates:
        #if the item isn't already on list, add it
        if item not in unique_candidates:
            unique_candidates.append(item)
    #for each name on unique list, gather info
    total = 0
    winning_name = []
    candidates_winning = 0
    for name in unique_candidates:
        total+= (candidates.count(name))
        print(name, candidates.count(name), round(100*candidates.count(name)/len(candidates)))
        if candidates.count(name) > candidates_winning:
            candidates_winning = candidates.count(name)
            winning_name.append(name)
    print (winning_name)
    print (total)
    #write to text file, brought for loop to ensure correct print
with open ("Py-Poll/pypollresults.txt", 'w') as f:
    total = 0
    f.write(str("Election Results")+'\n')
    f.write(str("---------------------------------------")+'\n')
    for name in unique_candidates:
        total += (candidates.count(name))
        pct="%.1f%%" % (100*candidates.count(name)/len(candidates))
        f.write(str(name)+'  '+ str(candidates.count(name))+'  '+ str(pct)+'\n')
    f.write(str("Total Votes: ") + str(total)+'\n')
    f.write(str("---------------------------------------)")+'\n')
    f.write(str("Winner:") + str(winning_name))
f.close