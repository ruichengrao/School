from random import random
from random import randint
board = []
enemy_board = []

class Ships:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
        self.health = size
        self.position = []
        self.direction = int(random() * 2) * 90
        empty_space = False
        
        row = 0
        column = 0

        while empty_space == False:
            empty_space = True
            if self.direction == 90:
                (row, column) = random_position(enemy_board, 0, self.size)
                random_position(enemy_board, self.size, 0)
                for i in range(self.size):
                    if enemy_board[row + i] [column] == 1:
                        empty_space = False
                        break

            elif self.direction == 0:
                (row, column) = random_position(enemy_board, self.size, 0)
                for i in range(self.size):
                    if enemy_board[row] [column + i] == 1:
                        empty_space = False
                        break


        if self.direction == 0:
            for i in range(self.size):
                self.position.append([row,column + i])

        elif self.direction == 90:
            for i in range(self.size):
                self.position.append([row,column + i])
            
                

       
def random_position(board, xBound, yBound):
                xCoord = randint(0, len(board)- 1 - xBound)
                yCoord = randint(0, len(board)- 1 - yBound)
                return (xCoord,yCoord)
for i in range(10):
    row = []
    for j in range(10):
        row.append("0")
    board.append(row)


for i in range(10):
    row = []
    for j in range(10):
        row.append("0")
    enemy_board.append(row)

def printBoard(board):
    for row in board:
       print(" ".join(row))
        

def printBoard(enemy_board):
    for row in enemy_board:
       print(" ".join(row))






ships = []
ships.append(Ships("Submarine", 1))
ships.append(Ships("Corsair", 2))
ships.append(Ships("Cruiser", 3))
ships.append(Ships("Battleship", 4))
ships.append(Ships("Carrier", 5))
print(ships)




def new_screen():
    
    print("Battleships!")
    print("My Board")
    printBoard(board)

previous_inputs_x = set()
previous_inputs_y = set()


def main():
    global x,y
    while True:
        new_screen()
        print("___________________")
        x = input("X-Coordinate:")
        y = input("Y-Coorinate:")

        if not x.isdigit() or not y.isdigit():
            print("Inputs are not intergers!")
        else: 
            x = int(x)
            y = int(y)
            if y > 9 or x > 9 or y < 0 or x < 0:
                print("Out of Bounds")
            elif board[y][x] != '0':
                print("This place has already been hit!")
            else:
                board[y][x] = 'X'
                print("You Missed!")




if __name__ == "__main__":
    main()
    


    