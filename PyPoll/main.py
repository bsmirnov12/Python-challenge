# Homework assignment (Part 2: "PyPoll")
# UT-TOR-DATA-PT-01-2020-U-C / 03-Python
# (c) Boris Smirnov

import os
import csv

# Debugging: determine if we must run the script in debug mode, i.e. with sample data
if ('DEBUG_MODE' in os.environ) and (os.environ['DEBUG_MODE'].upper() == 'TRUE'):
    debug_mode = True
else:
    debug_mode = False

# Initializing stats variables

total_votes = 0 # total number of votes
candidates = {} # every candidate is represented as a pair {candidate name: votes}

# Function for comparing candidates
# Used for sorting list of candidate names
def votes(name):
    return candidates[name]

# Reading CSV file

if debug_mode:
    src_fname = "election_data_sample.csv"
else:
    src_fname = "election_data.csv"

fname = os.path.join("Resources", src_fname)

with open(fname, newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    # Skipping the header
    next(csvreader)

    # Analysis loop
    for row in csvreader:
        name = row[2]
        total_votes += 1

        # Looking up a candidate and counting votes
        if name in candidates:
            candidates[name] += 1
        else:
            candidates[name] = 1

# All data has been read.
# Calculating rankings
rankings = sorted(candidates, key = votes, reverse = True)

# Generating report

report_str = "\nElection Results\n" + "-----------------------------------\n"
report_str += "Total Votes: {:,}\n".format(total_votes)
report_str += "-----------------------------------\n"
for name in rankings:
    report_str += "{:>12} : {:>6.2%} ({:>9,})\n".format(name, float(candidates[name]) / total_votes, candidates[name]) 
report_str += "-----------------------------------\n"
report_str += "Winner: " + rankings[0]
report_str += "\n-----------------------------------\n"

print(report_str)

# Dump report to the file
with open("report.txt", "w") as f:
    f.write(report_str)

# Done