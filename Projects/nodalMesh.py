def valuesToMatrix(r11, r22, r33, r12, r13, r23):
    
    matrix = [[r11, (-1*r12), (-1*r13)], [(-1*r12), (r22), (-1*r23)], [(-1*r13), (-1*r23), (r33)]]

    return matrix

def printMatrix(matrix):

    print("\n")
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
    
def delta(rg):
    
    r11 = float(input(f"Enter {rg}11 :"))
    r22 = float(input(f"Enter {rg}22 :"))
    r33 = float(input(f"Enter {rg}33 :"))
    r12 = float(input(f"Enter {rg}12 / {rg}21 :"))
    r13 = float(input(f"Enter {rg}13 / {rg}31 :"))    
    r23 = float(input(f"Enter {rg}23 / {rg}32 :"))

    matrix = valuesToMatrix(r11, r22, r33, r12, r13, r23)
    printMatrix(matrix)
    delt = determinant(matrix[0][0], matrix[0][1], matrix[0][2], matrix[1][0], matrix[1][1], matrix[1][2], matrix[2][0], matrix[2][1], matrix[2][2])

    return delt,matrix

def delta123(delt,matrix,iv):

    I1 = float(input(f"\nEnter {iv}1 :"))
    I2 = float(input(f"Enter {iv}2 :"))
    I3 = float(input(f"Enter {iv}3 :"))
    v = []
    print(f"\ndelta = {delt:.2f}\n")
    for i in range(3):

        temp1 = matrix[0][i]
        temp2 = matrix[1][i]
        temp3 = matrix[2][i]

        matrix[0][i] = I1
        matrix[1][i] = I2
        matrix[2][i] = I3

        deltnum = determinant(matrix[0][0], matrix[0][1], matrix[0][2], matrix[1][0], matrix[1][1], matrix[1][2], matrix[2][0], matrix[2][1], matrix[2][2])

        print(f"delta {i+1} = {deltnum:.2f}")
        v.append(deltnum/delt)

        matrix[0][i] = temp1
        matrix[1][i] = temp2
        matrix[2][i] = temp3

    return v



def main():

    nodalMesh = input("Do you want to solve nodal or mesh analysis : ").lower()

    if nodalMesh[0] == 'n':
        vi = "V"
        iv = "I"
        rg = "g"
    elif nodalMesh[0] == 'm':
        vi = "I"
        iv = "V"
        rg = "r"
    else:
        print("Error!!")

    delt,matrix = delta(rg)
    voltage = delta123(delt, matrix, iv)
    print("\n")
    for i in range(len(voltage)):
        print(f"{vi}{i+1} = {voltage[i]:.3f}")

if __name__ == "__main__":
    main()