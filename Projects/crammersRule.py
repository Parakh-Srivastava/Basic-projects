def printMatrix(matrix):
    
    print("\t\t\t\t MATRIX")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]} ",end="")
        print()

def value(matrix):

    print("\n")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = float(input(f"Enter the value of a{i + 1}{j + 1} : "))

    return matrix

def determinant3(a11,a12,a13,a21,a22,a23,a31,a32,a33):
    
    matrix = [[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]]
    
    delta = (((matrix[0][0] * matrix[1][1] * matrix[2][2]) + 
              (matrix[0][1] * matrix[1][2] * matrix[2][0]) + 
              (matrix[0][2] * matrix[1][0] * matrix[2][1])) - 
             ((matrix[0][2] * matrix[1][1] * matrix[2][0]) + 
              (matrix[1][2] * matrix[2][1] * matrix[0][0]) + 
              (matrix[2][2] * matrix[0][1] * matrix[1][0])))

    print(f"The determinant of the matrix is {delta}.")

def determinant2(a11,a12,a21,a22):

    matrix = [[a11,a12],[a21,a22]]
    
    delta = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    print(f"The determinant of the matrix is {delta}.")

def main():

    order = int(input("Enter the number mesh/nodes : "))

    match order:

        case 2:

            matrix = [["a11","a12"],["a21","a22"]]
            printMatrix(matrix)
            matrix = value(matrix)
            determinant2(matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1])

        case 3:

            matrix = [["a11","a12","a13"],["a21","a22","a23"],["a31","a32","a33"]]
            printMatrix(matrix)
            matrix = value(matrix)
            determinant3(matrix[0][0], matrix[0][1], matrix[0][2], matrix[1][0], matrix[1][1], matrix[1][2], matrix[2][0], matrix[2][1], matrix[2][2])

        case _:
            
            print("Only 2 and 3 mesh/node questions allowed .")

if __name__ == "__main__":
    main()