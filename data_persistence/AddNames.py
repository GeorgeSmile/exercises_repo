####Create a text file in your text editor and add some names of people on each line

####Read the names from the file in your application and populate an empty list with
##  the names 

####Print out the list

#####Did you notice something weird?

items = []
file = open("C:/vscode/Python/Exercises/Data_Persistence/people.txt", 'r')
for line in file.readlines():
    items.append(line.strip()) ## /n represents the new lines added when not adding .strip.


### Prints them onto separate lines
print (*items, sep = "\n")

# try:
#     if "Barry" in items:
#         print("Barry is in the list!")
# except:
#     print("Barry is not there!")

# finally:
#     print("Everyone is here!")
