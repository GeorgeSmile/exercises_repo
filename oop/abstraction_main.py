class PrintDetails:
    def __init__(self, name, age, city, salary):
        self.name = name
        self.age = age
        self.city = city
        self.salary = salary
    
    def derive_loan_capacity(self):
        if self.age > 30 and self.salary >= 50000:
            loan_capacity = "Loan available up to £100,000"
        elif self.age > 30 and self.salary >= 35000:
            loan_capacity = "Loan available up to £75,000"
        elif self.age > 21 and self.salary >= 21000:
            loan_capacity = "Loan available up to £50,000"
        else:
            loan_capacity = "No Loan available"
        return loan_capacity
    
    def print_details(self, loan_capacity):
        print(f' User name is {self.name}.\n Lives in {self.city}.\n Of age {self.age}.\n {loan_capacity}')