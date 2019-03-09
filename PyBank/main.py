import os
import csv

# reset csv iterator
def reset():
    data_file.seek(0)
    header = next(data_reader)

print('')
print('FINANCIAL ANALYSIS')
print('-----------------------------------------------------------')

# read csv
data_path = os.path.join('Resources', 'budget_data.csv')
with open(data_path, newline = '') as data_file:
    data_reader = csv.reader(data_file, delimiter = ',')
    header = next(data_reader)

# The total number of months included in the dataset
    row_count = sum(1 for row in data_reader)
    print(f'Total Months: {row_count}')

    reset()

# The net total amount of "Profit/Losses" over the entire period
    net_total = 0
    for row in data_reader:
        net_total += int(row[1])
    print(f'Net Profit: ${net_total}')

    reset()

# The average of the changes in "Profit/Losses" over the entire period
    setA = []
    setB = []
    average = 0
    for row in data_reader:
        setA.append(int(row[1]))

    reset()

    skip = next(data_reader)
    for row in data_reader:
        setB.append(int(row[1]))
    for i in range(85):
        average += int(setB[i]-setA[i])
    print(f'Average Change: ${round((average/85),2)}')

    reset()

# The greatest increase in profits (date and amount) over the entire period
    listA = []
    date_profit = []
    for row in data_reader:
        listA.append(int(row[1]))
        max_profit = max(listA)
        if int(row[1]) == max_profit:
            date_profit.append(row[0])
    print(f'Greatest Monthly Profit: ${max_profit} ({date_profit[-1]})')

    reset()

# The greatest decrease in losses (date and amount) over the entire period
    listB = []
    date_losses = []
    for row in data_reader:
        listB.append(int(row[1]))
        max_losses = min(listB)
        if int(row[1]) == max_losses:
            date_losses.append(row[0])
    print(f'Greatest Monthly Loss: ${max_losses} ({date_losses[-1]})')

    print('-----------------------------------------------------------')

# text file output
with open('output.txt', 'w') as file:
    file.write('FINANCIAL ANALYSIS\n')
    file.write('-----------------------------------------------------------\n')
    file.write(f'Total Months: {row_count}\n')
    file.write(f'Net Profit: ${net_total}\n')
    file.write(f'Average Change: ${round((average/85),2)}\n')
    file.write(f'Greatest Monthly Profit: ${max_profit} ({date_profit[-1]})\n')
    file.write(f'Greatest Monthly Loss: ${max_losses} ({date_losses[-1]})\n')
    file.write('-----------------------------------------------------------')
    file.close
