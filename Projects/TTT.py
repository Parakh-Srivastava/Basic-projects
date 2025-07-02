import random
gameboard = [[1,'|',2,'|',3],['-','+','-','+','-'],[4,'|',5,'|',6],['-','+','-','+','-'],[7,'|',8,'|',9]]
def gb():
    for i in range(0,5):
        for j in range(0,5):
            print(gameboard[i][j], end=' ')
        print()
def X_inputP():
    ch = True
    while(ch == True):
        X = int(input("X's turn :"))
        while (1 > X or X > 9):
            X = int(input("Enter numbers from 1 to 9 buddy :"))
        for i in range(0,5):
            for j in range(0,5):
                if(gameboard[i][j] == X ):
                    break
            if(gameboard[i][j] == X ):
                break
        if(gameboard[i][j] == X):
            gameboard[i][j] = 'X'
            ch = False
        else:
            print("invalid output !")
            ch = True
def X_inputC():
    ch = True
    while(ch == True):
        X = random.randint(1,9)
        while (1 > X or X > 9):
            X = int(input("Enter numbers from 1 to 9 buddy :"))
        for i in range(0,5):
            for j in range(0,5):
                if(gameboard[i][j] == X ):
                    break
            if(gameboard[i][j] == X ):
                break
        if(gameboard[i][j] == X):
            gameboard[i][j] = 'X'
            print("--------")
            print(f"X = {X}")
            ch = False
        else:
            ch = True
def O_input():
    ch = True
    while(ch == True):
        O = int(input("O's turn :"))
        while (1 > O or O > 9):
            O = int(input("Enter numbers from 1 to 9 buddy :"))
        for i in range(0,5):
            for j in range(0,5):
                if(gameboard[i][j] == O ):
                    break
            if(gameboard[i][j] == O ):
                break
        if(gameboard[i][j] == O):
            gameboard[i][j] = 'O'
            ch = False
        else:
            print("invalid output !")
            ch = True
def gameEndX():
    if(gameboard[0][0] == 'X' and gameboard[0][2] == 'X' and gameboard[0][4] == 'X'):
        print("X wins !!")
        return True
    elif(gameboard[2][0] == 'X' and gameboard[2][2] == 'X' and gameboard[2][4] == 'X'):
        print("X wins !!")
        return True
    elif(gameboard[4][0] == 'X' and gameboard[4][2] == 'X' and gameboard[4][4] == 'X'):
        print("X wins !!")
        return True
    elif(gameboard[0][0] == 'X' and gameboard[2][0] == 'X' and gameboard[4][0] == 'X'):
        print("X wins !!")
        return True
    elif(gameboard[0][2] == 'X' and gameboard[2][2] == 'X' and gameboard[4][2] == 'X'):
        print("X wins !!")
        return True
    elif(gameboard[0][4] == 'X' and gameboard[2][4] == 'X' and gameboard[4][4] == 'X'):
        print("X wins !!")
        return True
    elif(gameboard[0][0] == 'X' and gameboard[2][2] == 'X' and gameboard[4][4] == 'X'):
        print("X wins !!")
        return True
    elif(gameboard[0][4] == 'X' and gameboard[2][2] == 'X' and gameboard[4][0] == 'X'):
        print("X wins !!")
        return True
    else:
        return False
def gameEndO():
        if(gameboard[0][0] == 'O' and gameboard[0][2] == 'O' and gameboard[0][4] == 'O'):
            print("O wins !!")
            return True
        elif(gameboard[2][0] == 'O' and gameboard[2][2] == 'O' and gameboard[2][4] == 'O'):
            print("O wins !!")
            return True
        elif(gameboard[4][0] == 'O' and gameboard[4][2] == 'O' and gameboard[4][4] == 'O'):
            print("O wins !!")
            return True
        elif(gameboard[0][0] == 'O' and gameboard[2][0] == 'O' and gameboard[4][0] == 'O'):
            print("O wins !!")
            return True
        elif(gameboard[0][2] == 'O' and gameboard[2][2] == 'O' and gameboard[4][2] == 'O'):
            print("O wins !!")
            return True
        elif(gameboard[0][4] == 'O' and gameboard[2][4] == 'O' and gameboard[4][4] == 'O'):
            print("O wins !!")
            return True
        elif(gameboard[0][0] == 'O' and gameboard[2][2] == 'O' and gameboard[4][4] == 'O'):
            print("O wins !!")
            return True
        elif(gameboard[0][4] == 'O' and gameboard[2][2] == 'O' and gameboard[4][0] == 'O'):
            print("O wins !!")
            return True
        else:
            return False
def gameDraw():
    if(gameboard[0][0] != 1 and gameboard[0][2] != 2 and gameboard[0][4] != 3 and gameboard[2][0] != 4 and gameboard[2][2] != 5 and gameboard[2][4] != 6 and gameboard[4][0] != 7 and gameboard[4][2] != 8 and gameboard[4][4] != 9):
        if(gameEndO() == False and gameEndX() == False):
            print("The game is a draw !!")
            return True
CP = int(input("PvP = 1 || PvC = 2 :"))
print('Write the number where you want the respective symbol')
gb()
while (True):
    if(CP == 1):
        X_inputP()
    elif(CP == 2):
        X_inputC()
    gb()
    if(gameEndX() == True):
        break
    elif(gameEndO() == True):
        break
    elif(gameDraw() == True):      
        break
    O_input()
    gb()
    if(gameEndX() == True):
        break
    elif(gameEndO() == True):
        break
    elif(gameDraw() == True):      
        break