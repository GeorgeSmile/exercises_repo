# def my_function(*people):
#    for person in people:
#        print(person)

# my_function("Alice", "Bob", "John", 1, 2.3)


# def concatenate(**kwargs):
#    result = ""

#    for arg in kwargs.values():
#        result += arg
#    print(result)

# concatenate(a="Real", b="Python", c="Is", d="Great", e="!")


def concatenate(**kwargs):
  result = ""
  # Iterating over the Python kwargs dictionary
  for arg in kwargs.values():
    result += arg
  print (result)

concatenate(a="Real", b="Python", c="Is", d="Great", e="!")