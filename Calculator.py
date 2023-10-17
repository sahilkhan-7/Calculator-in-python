# # Calculator in Python

# while True :
#     print("\n--------------------------------------------------------------------------------")
#     print('''\nWhat you ant to perform 
#     1. Addition 
#     2. Subtraction
#     3. Multiplication
#     4. Division
#     0. Exit ''')
#     print("\n----------------------------------------")
#     n = int(input('\nEnter the number of task you want to perform : '))

#     if n == 1:
#          a = int(input('\nEnter first number : '))
#          b = int(input('Enter second number : '))
#          print('The sum is :', a+b)

#     elif n == 2:
#          a = int(input('\nEnter first number : '))
#          b = int(input('Enter second number : '))
#          print('The subtraction is :', a-b)

#     elif n == 3:
#         a = int(input('\nEnter first number : '))
#         b = int(input('Enter second number : '))
#         print('The multiplication is :', a*b)

#     elif n == 4:
#         a = int(input('\nEnter first number : '))
#         b = int(input('Enter second number : '))
#         print('The division is :', a/b)
#     elif n == 0:
#         exit(0)
#     else :
#         print('Please enter valid number.')


# Calculator in Python

while True :
    print("\n--------------------------------------------------------------------------------")
    print('''\nWhat you ant to perform 
    1. Addition 
    2. Subtraction
    3. Multiplication
    4. Division
    0. Exit ''')
    print("\n----------------------------------------")
    n = int(input('\nEnter the number of task you want to perform : '))

    match n:
        case 1:
            a = int(input('\nEnter first number : '))
            b = int(input('Enter second number : '))
            print('The sum is :', a+b)

        case 2:
            a = int(input('\nEnter first number : '))
            b = int(input('Enter second number : '))
            print('The subtraction is :', a-b)

        case 3:
            a = int(input('\nEnter first number : '))
            b = int(input('Enter second number : '))
            print('The multiplication is :', a*b)

        case 4:
            a = int(input('\nEnter first number : '))
            b = int(input('Enter second number : '))
            print('The division is :', a/b)
        case 0:
            exit(0)
        case _:
            print('Please enter valid number.')