import os
import csv
from decimal import Decimal

# Functions
def reset():
    data_file.seek(0)
    header = next(data_reader)

def counter(a):
    count = 0
    for row in data_reader:
        if row[2] == candidates[a]:
            count += 1
    running_total.append(count)
    print(f'{candidates[a]}: {round((count/vote_count*100), 0)}% ({count})')
    reset()

print('')
print('POLL ANALYSIS')
print('-----------------------------------------------------------')

# Read csv
data_path = os.path.join('Resources', 'election_data.csv')
with open(data_path, newline = '') as data_file:
    data_reader = csv.reader(data_file, delimiter = ',')
    header = next(data_reader)

# Total number of votes
    vote_count = sum(1 for row in data_reader)
    print(f'Total Votes: {vote_count}')
    print('-----------------------------------------------------------')

    reset()

# List of unique candidates
    candidates = []
    for candidate in data_reader:
            if candidate[2] not in candidates:
                candidates.append(candidate[2])
    print(f'Candidates: {candidates}')

    reset()

# Percentage and number of votes each candidate won
    running_total = []
    for i in range(len(candidates)):
        counter(i)
    print('-----------------------------------------------------------')

# Winner of the election based on popular vote
    winner = max(running_total)
    for i in range(len(candidates)):
        if winner == running_total[i]:
            print(f'WINNER: {candidates[i]}')
    print('')
