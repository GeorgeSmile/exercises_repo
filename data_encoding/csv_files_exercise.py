import csv


# Writes new row with field names and a dictionary person in the keys and values
with open('C:/vscode/Python/Exercises/data_encoding/test_names.csv', mode='w') as file:
    fieldnames = ['first_name', 'last_name', 'age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
        'first_name': 'Jane',
        'last_name': 'Smith',
        'age': 60
    })
    

# Appends rows to the file
with open('C:/vscode/Python/Exercises/data_encoding/test_names.csv', mode='a+') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['Mike', 'Wazowski', 40])
    writer.writerow(['Joe', 'Bloggs', 40])