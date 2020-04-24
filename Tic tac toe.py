#board design
board = ['-','-','-',
        '-','-','-',
         '-','-','-']
#3 Global Variables
current_player = 'x'
game_is_going_on = True
Winner = None

#Function to display board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

#Function for game structure
def play_game():
    #FIrst display the board
    display_board()
    #check if game is going on /by default game is On(True)
    while game_is_going_on:
        #ask player to make a choice on board
        handle_turn(current_player)

        #check if winner or tie to verify game
        check_if_game_over()

        #is game is going on change turn of player
        flip_player()

    #call the global variable(Winner) to announce winner
    if Winner == "x" or Winner == "o":
        print(Winner +" won.")
    elif Winner == None:
        print("Tie.")

#Function to change player
def flip_player():
    #Global Variable
    global current_player
    if current_player == 'x':
        #change Global variable value
        current_player = 'o'
    elif current_player == 'o':
        current_player = 'x'


def handle_turn(player):
    position = input("choose between 1-9: ")
    valid = False
    while not valid:


        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("choose between 1-9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("you an't go there.")

    board[position] = player
    display_board()


def check_if_game_over():
    check_winner()
    check_tie()

def check_winner():
    global Winner
    row_winner = check_row_winner()
    columns_winner = check_columns_winner()
    diagonals_winner = check_diagonals_winner()

    if row_winner:
        Winner = row_winner
    elif columns_winner:
        Winner = columns_winner
    elif diagonals_winner:
        Winner = diagonals_winner
    else:
        Winner = None


def check_row_winner():
    global game_is_going_on

    row_1 = board[0] == board[1] == board[2]!= '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1 or row_2 or row_3:
        game_is_going_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_columns_winner():
    global game_is_going_on

    columns_1 = board[0] == board[3] == board[6]!= '-'
    columns_2 = board[1] == board[4] == board[7] != '-'
    columns_3 = board[2] == board[5] == board[8] != '-'

    if columns_1 or columns_2 or columns_3:
        game_is_going_on = False
    if columns_1:
        return board[0]
    elif columns_2:
        return board[1]
    elif columns_3:
        return board[2]
    else:
        return None

def check_diagonals_winner():
    global game_is_going_on

    diagonals_1 = board[0] == board[4] == board[8]!= '-'
    diagonals_2 = board[2] == board[4] == board[6] != '-'

    if diagonals_1 or diagonals_2:
        game_is_going_on = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]
    else:
        return None

def check_tie():
    global game_is_going_on
    if '-' not in board:
        game_is_going_on = False
        return True
    else:
        return False

play_game()