# Snake Game Board Renderer
board = [["." for c in range(5) ] for r in range(5)]
board[2][3] = 'F'
row = int(input("Enter row coordinate (0-4): "))
col = int(input("Enter col coordinate (0-4): "))
ate_food = False
if(row==2 and col==3):
    ate_food = True
board[row][col] = "S"

for board_row in board:
    print(" ".join(board_row))
if ate_food:
    print("Yum! The snake ate the food!")




