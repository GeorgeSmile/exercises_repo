list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]

for fruit1 in list1:
    for fruit2 in list2:
        if fruit1 == fruit2:
            print(f"{fruit1} True")
            
            
####### Other method

list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]

f_list = []

for fruit1 in list1:
    for fruit2 in list2:
        if fruit1 == fruit2:
            f_list.append(fruit1)

print(f_list)