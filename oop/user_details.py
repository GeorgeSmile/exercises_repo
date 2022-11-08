from abstraction_main import PrintDetails 

user_name = 'James'
user_age = 25
user_city = 'Manchester'
user_salary = 60000

printing_obj = PrintDetails(user_name, user_age, user_city, user_salary)
loan_value = printing_obj.derive_loan_capacity()
printing_obj.print_details(loan_capacity=loan_value)
