import os
import csv

electiondata_path = os.path.join('Resources', 'election_data.csv')

with open(electiondata_path, newline='') as electiondata_file: 
    electiondata_reader= csv.reader(electiondata_file, delimiter=",")

    # Transfer contents of csv to a list so that multiple loops can be run on it.
    data = list(electiondata_reader)
    # Exclude Headers from list
    data.pop(0)

    # 
    total_votes = 0
    candidate_list = []
    votes_list = []
    votes = 0

    for row in data:
        total_votes = total_votes + 1

        if row[2] not in candidate_list:
            candidate_list.append(row[2])

    print ("Election Results")
    print ("------------------------")
    print (f"Total Votes: {total_votes}")
    print ("------------------------")    
        
    length = len(candidate_list)
    votes_list = []
    winning_percent=[]

    for i in range(length):
        votes = 0
        for row in data:
            if row[2] == str(candidate_list[i]):
                votes = votes+1
        votes_list.append(votes)
        percent = format(((votes_list[i]/total_votes)*100),".3f")
        winning_percent.append(percent)
        print(f"{candidate_list[i]}: {winning_percent[i]}%  ({votes_list[i]})")

    print ("------------------------")

    winner_index = votes_list.index(max(votes_list))
    print (f"Winner:  {candidate_list[winner_index]}")
    print ("------------------------")

    outfile = 'Analysis/output.txt'
    with open(outfile,'w') as text:
        lines = text.write("Election Results\n")
        lines = text.write("------------------------\n")
        lines = text.write(f"Total Votes: {total_votes}\n")
        lines = text.write("------------------------\n")
        for i in range(length):
            lines = text.write(f"{candidate_list[i]}: {winning_percent[i]}%  ({votes_list[i]})\n")
        lines = text.write("------------------------\n")
        lines = text.write(f"Winner:  {candidate_list[winner_index]}\n")
        lines = text.write("------------------------\n")