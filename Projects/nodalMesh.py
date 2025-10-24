def valuesToMatrix(r11, r22, r33, r12, r13, r23):
    
    matrix = [[r11, (-1*r12), (-1*r13)], [(-1*r12), (r22), (-1*r23)], [(-1*r13), (-1*r23), (r33)]]

    return matrix

def printMatrix(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]} ",end="")
        print()

def determinant(a11,a12,a13,a21,a22,a23,a31,a32,a33):
    
    matrix = [[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]]
    
    delta = (((matrix[0][0] * matrix[1][1] * matrix[2][2]) + 
              (matrix[0][1] * matrix[1][2] * matrix[2][0]) + 
              (matrix[0][2] * matrix[1][0] * matrix[2][1])) - 
             ((matrix[0][2] * matrix[1][1] * matrix[2][0]) + 
              (matrix[1][2] * matrix[2][1] * matrix[0][0]) + 
              (matrix[2][2] * matrix[0][1] * matrix[1][0])))
    
    return delta
    
def delta():
    
    r11 = float(input("Enter r11 :"))
    r22 = float(input("Enter r22 :"))
    r33 = float(input("Enter r33 :"))
    r12 = float(input("Enter r12 / r21 :"))
    r13 = float(input("Enter r13 / r31 :"))    
    r23 = float(input("Enter r23 / r32 :"))

    matrix = valuesToMatrix(r11, r22, r33, r12, r13, r23)
    delt = determinant(matrix[0][0], matrix[0][1], matrix[0][2], matrix[1][0], matrix[1][1], matrix[1][2], matrix[2][0], matrix[2][1], matrix[2][2])

    return delt,matrix

def delta123(delt,matrix):

    I1 = float(input("Enter V/I 1 :"))
    I2 = float(input("Enter V/I 2 :"))
    I3 = float(input("Enter V/I 3 :"))

    v = []

    initialMatrix = matrix

    print()

    for i in range(3):

        matrix[0][i] = I1
        matrix[1][i] = I2
        matrix[2][i] = I3

        deltnum = determinant(matrix[0][0], matrix[0][1], matrix[0][2], matrix[1][0], matrix[1][1], matrix[1][2], matrix[2][0], matrix[2][1], matrix[2][2])

        print(f"delta {i+1} = {deltnum}")
        v.append(deltnum/delt)
        
        matrix = initialMatrix

    return v



def main():

    delt,matrix = delta()

    voltage = delta123(delt, matrix)

    for i in range(len(voltage)):
        print(f"Voltage / current {i+1} = {voltage[i]}")

if __name__ == "__main__":
    main()