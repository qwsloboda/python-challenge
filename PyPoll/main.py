import os
import csv
import operator

csvpath = os.path.join( '..', 'python-challenge' ,'PyPoll' ,'Resources', 'election_data.csv')

print("opening", csvpath)
voter_id = []
county = []
candidates = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])


    total_votes = len(voter_id)

    print("Election Results")
    print("------------------------")
    print("Total Votes: " + str(total_votes))
    print("------------------------")

    uniqueCandidates = []
    votesForCan = {}
    votesForCanFormat = {}
    
    for candidate in candidates: 
        if not candidate in uniqueCandidates:
            uniqueCandidates.append(candidate)
            totalCanVotes = candidates.count(candidate)
            votesForCanFormat.update( [(candidate, (str(round((totalCanVotes / total_votes * 100), 3)) + "%" + " (" + str(totalCanVotes) + ")"))])
            votesForCan.update( [(candidate,totalCanVotes)])
    for key, value in votesForCanFormat.items():
        print(key, " : ", value)

    print("------------------------")
    winner = max(votesForCan.items(), key=operator.itemgetter(1))[0]
    print("Winner: " + winner)

    print("------------------------")



    
    

#print(uniqueCandidates)   
#print(votesForCan)
  

    
    








