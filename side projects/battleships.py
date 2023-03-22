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
    printBoard(board)


def main():
    new_screen()

if __name__ == "__main__":
    main()


print("My Board")

print("-------------------")
print("Enemy Board")
printBoard(enemy_board)


    