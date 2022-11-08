items = {}
file = open("C:/vscode/Python/Exercises/Data_Persistence/names.txt", 'r')


for line in file.readlines():
    file = sum(1 for v in items.values() if v == 0)

print(items)