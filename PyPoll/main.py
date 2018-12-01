#Dependencies

import csv

import os



#Load files

csvpath = os.path.join("Resources",
"election_data.csv")

pathout = os.path.join("Resources",
"Election Analysis")



#Variables I need to use

votes = 0

winner_votes = 0

total_candidates =
0

greatest_votes = ["", o]

candidate_options = []

candidate_votes{}





#read the data

with 
open(csvpath) 
as election_data:

    reader = csv.DictReader(election_data)



#Create loop to do work within to find the finish products

    for row
in reader:

        votes = votes
+ 
1

        total_candidates = row["Candidate"]



        if row["Candiate not in candiate_options"]:

            candidate_options.append(row["Candidate"])

            candidate_votes[row["Candidate"]]
= 
1



        else



            candidate_votes[row["Candidate"]]
= candidates_votes[row["Candidate"]]
+ 
1



    #print information

     print()

    print()

    print()

    print("Election Results")

    print("-------------------------")

    print("Total Votes "
+ 
str(votes))

    print("-------------------------")

#results

    for candidate
in candidate_votes:

        print(candidate
+ 
" " +
str(round(((candidate_votes[candidate]/votes)*100)))
+ 
"%" +
" (" 
+ str(candidate_votes[candidate])
+ 
")") 

        candidate_results = (candidate
+ 
" " +
str(round(((candidate_votes[candidate]/votes)*100)))
+ 
"%" +
" (" 
+ str(candidate_votes[candidate])
+ 
")") 

    

candidate_votes



winner =
sorted(candidate_votes.items(),
key=itemgetter(1),
reverse=True)



#results

print("-------------------------")

print("Winner: "
+ 
str(winner[0]))

print("-------------------------")











# Output Files

with 
open(pathout, 
"w") as txt_file:

    

    txt_file.write("Election Results")

    txt_file.write("\n")

    txt_file.write("-------------------------")

    txt_file.write("\n")

    #txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")

    txt_file.write(str(winner))

    txt_file.write("\n")

    txt_file.write("-------------------------")

    txt_file.write("\n")

    txt_file.write("Winner: "
+ 
str(winner[0]))

    txt_file.write("\n")

    txt_file.write("Total Votes "
+ 
str(votes))
