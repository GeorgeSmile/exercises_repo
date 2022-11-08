import csv

# Reads csv file as strings
# with open('C:/vscode/Python/Exercises/data_encoding/ford_escort.csv', 'r') as file:
#     reader = csv.reader(file, delimiter=',')
#     for row in reader:
#         print(row)

## Prints csv file as a dictionary
# with open('C:/vscode/Python/Exercises/data_encoding/ford_escort.csv', 'r') as file:
#     csv_file = csv.DictReader(file)
#     for row in csv_file:
#         print(row)

## Adds new row of first name, last name and age
# with open('C:/vscode/Python/Exercises/data_encoding/ford_escort.csv', mode='a') as file:
#     writer = csv.writer(file, delimiter=',')
##    instruct the write to write a row
#     writer.writerow(['Joe', 'Bloggs', 40])
#     writer.writerow(['Jane', 'Smith', 50])

## Writes new row 
with open('C:/vscode/Python/Exercises/data_encoding/ford_escort.csv', mode='a') as file:
    fieldnames = ['first_name', 'last_name', 'age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
        'first_name': 'Jane',
        'last_name': 'Smith',
        'age': 60
    })


