# Write a Python program to compute following operations on Matrices.
#Take matrix input in a form of list and display in the form of matrix
# Perform operations on matrices
# Addition of two matrices
# Subtraction of two matrices
# Multiplication of two matrices
# Transpose of a matrix


#matrix initialization global list
M1 = []
M2 = []
M = []

def input_matrix(M1,M2): #taking input and displaying as a matrix

    print("Enter the elements in first matrix")
    for i in range(r1):
        row = []
        for j in range(c1):
            y = int(input())
            row.append(y)
        M1.append(row)
    print("Matrix accepted")
    print("Enter the elements in second matrix")
    for i in range(r2):
        row = []
        for j in range(c2):
            y = int(input())
            row.append(y)
        M2.append(row)
    print("Matrix accepted")

    print("Do you want a display of both matrices?")
    ch = input("Enter Y/N\n")
    if ch == "Y":
        print("First matrix entered is")
        for i in range(r1):
            for j in range(c1):
                print(M1[i][j], end=" ")
            print()

        print("Second matrix entered is")
        for i in range(r1):
            for j in range(c1):
                print(M2[i][j], end=" ")
            print()
    else:
        print("OK")

# input_matrix(M1,M2)

def addition(M1,M2): #addition of matrices
    if r1 == r2 and c1 == c2:
        input_matrix(M1,M2)
        addition = []
        for i in range(r1):
            sum = []
            for j in range(c1):
                value = M1[i][j] + M2[i][j]
                sum.append(value)
            addition.append(sum)

        print("The Addition of matrix 1 and 2 is")
        for i in range(r1):
            for j in range(c1):
                print(addition[i][j],end = " ")
            print()
# addition(M1,M2)

def subtraction(M1,M2): #subtraction of matrices
    if r1 == r2 and c1 == c2:
        input_matrix(M1,M2)
        subtraction = []
        for i in range(r1):
            sub = []
            for j in range(c1):
                value = M1[i][j] - M2[i][j]
                sub.append(value)
            subtraction.append(sub)

        print("The Subtraction of matrix 1 and 2 is")
        for i in range(r1):
            for j in range(c1):
                print(subtraction[i][j],end = " ")
            print()
# subtraction(M1,M2)

def multiplication(M1,M2): #multiplication of matrices
    if r1 == c2:
        final_multiplication=[]
        input_matrix(M1,M2)
        for i in range(r1):
            mul = []
            for j in range(c1):
                result = 0
                for k in range(c1):
                    result = result + (M1[i][k]*M2[k][j])
                mul.append(result)
            final_multiplication.append(mul)

        print("The Multiplication of matrix 1 and 2 is")
        for i in range(r1):
            for j in range(c1):
                print(final_multiplication[i][j],end = " ")
            print()
# multiplication(M1,M2)

def transpose(M): #transpose of a matrix
    print("Enter the order of matrix")
    r = int(input("Enter the number of rows of Matrix"))
    c = int(input("Enter the number of columns Matrix"))
    print("Enter the elements of matrix")
    for i in range(r):
        transpose = []
        for j in range(c):
            y = int(input())
            transpose.append(y)
        M.append(transpose)
    print("Matrix accepted")

    def display(M,r,c):
        print("The matrix is")
        for i in range(r):
            for j in range(c):
                print(M[i][j],end=" ")
            print()

    def transposed(M,r,c):
        print("The transposed matrix is")
        for i in range(r):
            for j in range(c):
                print(M[j][i],end=" ")
            print()

    display(M,r,c)
    transposed(M,r,c)
    
# transpose()

while True:
    print("Following operations can be performed on matrices\n1)Addition of two matrices\n2)Subtraction of two matrices\n3)Multiplication of two matrices\n4)Transpose of a matrix")
    choice = int(input("Enter your choice:"))
    if (choice == 1 or choice == 2 or choice == 3):
        print("Enter the order of matrix")
        r1 = int(input("Enter the number of rows in first matrix "))
        c1 = int(input("Enter the number of columns in first matrix "))
        r2 = int(input("Enter the number of rows in second matrix "))
        c2 = int(input("Enter the number of columns in second matrix "))

    if choice == 1:
        addition(M1,M2)
    elif choice == 2:
        subtraction(M1,M2)
    elif choice == 3:
        multiplication(M1,M2)
    elif choice == 4:
        transpose(M)
    else:
        print("Invalid Input\nTry entering a valid choice")