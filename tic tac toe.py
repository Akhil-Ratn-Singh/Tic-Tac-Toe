"""
print board
quit condition
take user input
check user input
convert user input into coordinates
check if coordinates position is taken
add user input to board(coordinates)
check if won
switch player

"""


board = [
    ["#", "#", "#"],
    ["#", "#", "#"],
    ["#", "#", "#"]
]


user = True  # if True user is "X" else user is "O"


def print_board(board):
    for row in board:
        for slot in row:
            print(f" {slot} ",end="")
        print()


def quit(user_input):
    if user_input.lower() == "q":
        print("Thanks for playing !!!")
        return True
    return False


def check_input(user_input):
    if not user_input.isnumeric():
        print("enter a number")
        print("Please try again")
        return False
    if int(user_input) > 9 or int(user_input) < 1:
        print("enter a number between 1-9")
        print("Please try again")
        return False
    return True


def coordinates(user_input):
    row = int(user_input/3)
    column = int(user_input)
    if user_input > 2:
        column = int(user_input % 3)
    return (row,column)


def is_taken(coords, board):
  row = coords[0]
  col = coords[1]
  if board[row][col] != "#":
    print("This position is already taken.")
    print("Please try again")
    return True
  else: return False


def add_to_board(coords,board,active_user):
    row, column = coords[0], coords[1]
    board[row][column] = active_user


def current_user(user):
    if user:
        return "X"
    return "O"


def check_winner(user,board):
    if check_row(user,board):
        return True
    if check_column(user,board):
        return True
    if check_diagonal(user,board):
        return True
    return False


def check_row(user,board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
        if complete_row:
            return True
    return False


def check_column(user,board):
    for column in range(3):
        complete_column = True
        for row in range(3):
            if board[row][column] != user:
                complete_column = False
                break
        if complete_column:
            return True
    return False


def check_diagonal(user,board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    return False


while True:
    active_user= current_user(user)
    print_board(board)
    user_input= input("Please enter a number 1-9 or press q to quit: ")
    if quit(user_input): break
    if not check_input(user_input): continue
    user_input = int(user_input) - 1
    coords = coordinates(user_input)
    if is_taken(coords,board): continue
    add_to_board(coords,board,active_user)
    if check_winner(active_user,board):
        print_board(board)
        print(f"{active_user} Won! ")
        break
    user = not user



