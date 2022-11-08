f = int (input("Enter Farenheit temperature: "))
c = int (input("Enter Celsius temperature: "))

farenheit_convert = (f - 32) * (5/9)
print(f"Farenheit converted to Celsius is: {farenheit_convert}")
celsius_convert = (c * 1.8) + 32
print(f"Celsius converted to Farenheit is: {celsius_convert}")