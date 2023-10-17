
def Fact(n):
    if n == 0:
        return 1
    else :
        return n * Fact(n - 1)

def matrix():

    def input_matrix():
        matrix = []
        r = int(input('Enter the number of rows: '))
        c = int(input('Enter the number of column: '))
        for i in range(r):
            rows = []
            for j in range(c):
                value = int(input(f'Enter the value at position [{i+1}][{j + 1}]: '))
                rows.append(value)
            matrix.append(rows)
        return matrix, r, c

    m1, r1, c1 = input_matrix()
    print('For second matrix:')
    m2, r2, c2 = input_matrix()

    def matrix_mul(m1, m2):
        mul_mat = []
        element = 0
        if len(m1[0]) == len(m2):
            for i in range(r1):
                for j in range(c2):
                    element += m1[i][j]*m2[j][i]
        else:
            return f'Size of matrixes doesn\'t match for multiplication.'

    # mul_mat = matrix_mul(m1, m2)
    # input_matrix()


    def matrix_addition(m1, m2):
        addition_matrix = []
        if len(m1[0]) == len(m2):
            for i in range(r1):
                raw = []
                for j in range(c1):
                    raw.append(m1[i][j] + m2[i][j])
                addition_matrix.append(raw)
        return addition_matrix

    print(matrix_addition(m1, m2))


def simple():
    x = True
    while x :
        print("\n--------------------------------------------------------------------------------")
        print('''\nWhat you ant to perform 
        1. Addition 
        2. Subtraction
        3. Multiplication
        4. Division
        5. Back
        0. Exit ''')
        print("\n----------------------------------------")
        n = int(input('\nEnter the number of task you want to perform: '))

        match n:
            case 1:
                a = int(input('\nEnter first number: '))
                b = int(input('Enter second number: '))
                print('The sum is :', a+b)

            case 2:
                a = int(input('\nEnter first number: '))
                b = int(input('Enter second number: '))
                print('The subtraction is :', a-b)

            case 3:
                a = int(input('\nEnter first number : '))
                b = int(input('Enter second number : '))
                print('The multiplication is :', a*b)

            case 4:
                a = int(input('\nEnter first number: '))
                b = int(input('Enter second number: '))
                print('The division is :', a/b)
                
            case 0:
                exit(0)
            case _:
                print('Please enter valid number.')

matrix()