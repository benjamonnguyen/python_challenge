import os
import csv
from decimal import Decimal

# Functions
def reset():
    data_file.seek(0)
    header = next(data_reader)

def super_print(a):
    print(a)
    print(a, file=open('output.txt', 'a'))

def counter(a):
    count = 0
    for row in data_reader:
        if row[2] == candidates[a]:
            count += 1
    running_total.append(count)
    super_print(f'{candidates[a]}: {round((count/vote_count*100), 0)}% ({count})')
    reset()

print('')
super_print('POLL ANALYSIS')
super_print('-----------------------------------------------------------')

# Read csv
data_path = os.path.join('Resources', 'election_data.csv')
with open(data_path, newline = '') as data_file:
    data_reader = csv.reader(data_file, delimiter = ',')
    header = next(data_reader)

# Total number of votes
    vote_count = sum(1 for row in data_reader)
    super_print(f'Total Votes: {vote_count}')
    super_print('-----------------------------------------------------------')

    reset()

# List of unique candidates
    candidates = []
    for candidate in data_reader:
            if candidate[2] not in candidates:
                candidates.append(candidate[2])
    super_print(f'Candidates: {candidates}')

    reset()

# Percentage and number of votes each candidate won
    running_total = []
    for i in range(len(candidates)):
        counter(i)
    super_print('-----------------------------------------------------------')

# Winner of the election based on popular vote
    winner = max(running_total)
    for i in range(len(candidates)):
        if winner == running_total[i]:
            super_print(f'WINNER: {candidates[i]}')
    print('')
