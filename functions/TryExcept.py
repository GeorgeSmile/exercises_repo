x = "hello this is a test "
y = str(3)

result = x + y

try:
    print(result)
except:
    print("An exception error occured")

try:
    print(y)
except:
    print("A new exception has occured")
else:
    print("Nothing went wrong")
finally:
    print("the try-except has finished")