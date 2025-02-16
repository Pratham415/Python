# Problem 1: Salary Bonus Calculation
# Description: Write a program that calculates the annual bonus for an employee
# based on their years of service and performance rating. The rules are:
# • If years of service are greater than 10 and performance rating is ”Excellent,” bonus is 20% of salary.
# • If years of service are between 5 and 10 and performance rating is ”Good,”
# bonus is 10% of salary.
# • If years of service are less than 5 and performance rating is ”Average,”
# bonus is 5% of salary.
# • Otherwise, no bonus.
# Input: years_of_service = 8, performance_rating = "Good", salary =
# 50000
# Output: ”Bonus: 5000”

# years_of_service = int(input("Enter the yera : "))
# perf = input("Enter the performance : ")
# salary = int(input("Enter the salary : "))

# if(perf == "Excellent") and (years_of_service > 10): 
#     salary = salary * .2
#     print(salary)

# if(perf == "Good") and (5 < years_of_service <= 10): 
#     salary = salary * .1
#     print(salary)

# if(perf == "Average") and (years_of_service <= 5): 
#     salary = salary * .05
#     print(salary)


## 2 ---------------------------

# Problem 4: User Authentication System
# Description: Write a program that checks if a user’s inputted username and
# password match the stored values. The rules are:
# • If both username and password match, print ”Access granted.”
# • If username matches but the password does not, print ”Incorrect password.”
# • If neither matches, print ”Invalid username and password.”
# Input: stored_username = "user1", stored_password = "pass123",
# input_username = "user1", input_password = "pass124"
# # Output: ”Incorrect password”

# userN = "Pratham04"
# passw = "Venom@123"
# username = input("Enter the username :  ")
# password = input("enter the password :  ")

# if username == userN and passw == password :
#     print("Access granted !")
# else:
#     print("Incorrect password !")

## 3--------------------------------

# Problem 5: Utility Bill Calculation
# Description: Write a program that calculates the monthly utility bill for electricity based on the number of units consumed. The billing rules are:
# • For the first 100 units, the cost is $0.5 per unit.
# • For the next 100 units (101-200), the cost is $0.75 per unit.
# • For units above 200, the cost is $1.0 per unit.
# • Additionally, if the total bill exceeds $100, add a surcharge of 10%.
# Input: units_consumed = 250
# Output: ”Total Bill: $162.5”

# units = int(input("Enter the number of units : "))
# if units == 100:
#     bill = units * .5
#     print(f"The total bill = {bill} ")
# elif units > 100 and units <= 200:
#     bill = units * .75
#     print(f"The total bill = {bill}")
# else:
#     bill = units * 1
#     print(f"The total bill = {bill} ")