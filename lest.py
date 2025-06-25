gameboard = [[1,'|',2,'|',3],['-','+','-','+','-'],[4,'|',5,'|',6],['-','+','-','+','-'],[7,'|',8,'|',9]]
def gb():
    for i in range(0,5):
        for j in range(0,5):
            print(gameboard[i][j], end=' ')
        print()
def x_input():
    O = int(input("O's turn :"))
    while (1 > O or O > 9):
        O = int(input("Enter numbers from 1 to 9 buddy :"))
    for i in range(0,5):
        for j in range(0,5):
            if(gameboard[i][j] == O):
                gameboard[i][j] = 'O'
x_input()
gb()