board = []
enemy_board = []

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


    