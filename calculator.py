def welcome():
    print('Hey dude lets get us know')
    name = input('What is your name?\n')
    print('Hi, %s come in to calculator' % name)

def calculate():
    operation = input('''
Type the math operation u would like to complete:
+ addition
- subtraction
* multiplication
/ division
% modulo
''')

    number_1 = int(input('Enter your 1st number: '))
    number_2 = int(input('Enter your 2nd number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == '%':
        print('{} % {} = '.format(number_1,number_2))
        print(number_1 % number_2)

    else:
        print('U have not entered a valid operator, pls run the program again')

    again()

def again():
    calc_again = input('''
Would u like to calc again?
PLS type Y for YEP and N for NOPE
''')
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Would u like a cup of smth?')
    else:
        again()
welcome()
calculate()




# # This function adds two numbers
# def add(x, y):
#     return x + y
#
# # This function subtracts two numbers
# def subtract(x, y):
#     return x - y
#
# # This function multiplies two numbers
# def multiply(x, y):
#     return x * y
#
# # This function divides two numbers
# def divide(x, y):
#     return x / y
#
#
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
#
# while True:
#     # Take input from the user
#     choice = input("Enter choice(1/2/3/4): ")
#
#     # Check if choice is one of the four options
#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#
#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))
#
#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))
#
#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))
#
#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
#         break
#     else:
#         print("Invalid Input")

# Define our function