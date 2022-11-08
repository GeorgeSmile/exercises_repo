age = int(input("What is your age: "))
salary = int(input("What is your salary (£): "))

if age > 30 and salary >= 50000:
    print("Loan available up to £100,000")
elif age > 30 and salary >= 35000:
    print("Loan available up to £75,000")
elif age > 21 and salary >= 21000:
    print("Loan available up to £50,000")
else:
    print("No Loan available")