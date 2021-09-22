# #lesson 97
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return
#     first_name = f_name.title()
#     last_name = l_name.title()
#     return f"{first_name} {last_name}"
#
#
# print(format_name(input("What is your first name: ?"), input("What is your last name?")))
#
#

#Lesson 99

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 #print("Leap year.")
#                 return True
#             else:
#                 #print("Not leap year.")
#                 return False
#         else:
#             #print("Leap year.")
#             return True
#     else:
#         #print("Not leap year.")
#         return False
#
# def days_in_month(year, month):
#     if month > 12 or month <1:
#         return "Invalid month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]
#
#
#
# #🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

#lesson 100

# def test_fun():
#     '''Ololo'''
#     print("lol")
# test_fun()

#lesson101

#calculator
from art import logo

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    print(logo)
    num1 = float(input("What is your first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is your next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Type 'y' to continue calculating or 'n' to exit. To start a new calculation enter") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
