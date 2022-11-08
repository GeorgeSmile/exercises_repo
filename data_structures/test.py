###### strings

from xml.sax.xmlreader import InputSource


name = "George"
last_name = "Whittall-Weston"

print(f"Hi, my name is {name} {last_name}")

##### integers

x = 42
y = 2

product = x*y

print(f"The product of {x} and {y} is {product}")

##### lists

people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

third_element = people[2] 

print(third_element)

print(people[2:-1])

print(people[0] == people[-1])


###### input
enter_name = input("Enter name: ")
fave_number = input("Enter favourite number: ")
age = input("Enter age: ")

if fave_number == age:
    print("Your favourite number is the same as your age!")
else:
    print("Your favourite number is not equal to your age.")

