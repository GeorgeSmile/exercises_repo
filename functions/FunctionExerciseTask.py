#1. Create a function that takes two numbers as arguments and return the sum. 
# Print the result.
#2. Extend the above by passing an arbitrary amount of integers to a function 
# and return the result. Print the result. Hint: use `*args`.
#3. Pass an arbitrary amount of named arguments to a function and create a dictionary. 
# The keys will be the names of the arguments and the values are assigned 
# values of the named arguments. Hint: use `**kwargs`.
#4. Create a scientific/basic calculator that makes use of separate functions to 
# perform calculations, such as: `add`, `divide`, `area_of_a_circle` etc...
#5. Add some form of user interface to allow the user to perform calculations
#6. Print out a nice result / log to the screen



####
#def add_numbers(a, b, c):
#    return a + b + c
#result = add_numbers(1, 2, 3)
#print(result)

def x(a, b):
    return a + b
result = x(4, 8)

print(result)

####
#def x(*args, **kwargs):
#    print(args)
#    print(kwargs)

#courses = ['Math', 'Art']
#info = {'name': 'John', 'age': 22}

#x(*courses, **info)

####
#def num(*args):
#    print(args)

#extend = [1, 2, 3]

#num(*extend)