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