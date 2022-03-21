# 7. TIC-TAC-TOE

# Write a Tic-Tac-Toe program that allows two people to play the game against each other.
#  In turn, ask each player which row and column they want to play. Make sure that the program checks if that row/column combination is empty.
#  When a player has won, end the game. When the whole board is full and there is no winner, announce a draw.

# This is a fairly long program to write (60 lines or so). It will definitely help to use some functions. I recommend that you create:
# a function display_board() that gets the board as a parameter and displays it
# a function getRowCol() that asks for a row or a column (de- pending on a parameter) and checks whether the user entered a legal value
# a function winner() that gets the board as an argument and checks if there is a winner.
# Keep track of who the current player is using a global variable player that you can pass to a function as an argument if the function needs it.
#  I also use the function opponent(), which takes the player as an argument and returns the opponent. I use that to switch players after each move.
#  The main program will be something along the lines of (in pseudo-code):


#board
#display board
#play game
#handle turn
#check win
 #check rows
 #check colums
 #check diagonals
#check tie
#flip player


#board

#-------golbal variable---------------------------

game_still_going=True


#who won or tie?
winner =None

#
current_player="X"


board= ["-","-","-",
        "-","-","-",
        "-","-","-"]


def display_board():
    print(board[0] + "|" + board[1] + "|" +board[2] )
    print(board[3] + "|" + board[4] + "|" +board[5] )
    print(board[6] + "|" + board[7] + "|" +board[8] )

def play_game():
    
    #display initial board
    display_board()

    while game_still_going:

        #handle a single turn of an arbitrary player
        handle_turn(current_player)

        #check if the game has ended
        check_if_game_over()

        #Flip to the other player
        flip_player()

    #the game has ended
    if winner =="X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print(" Tie.")


    


def handle_turn(player):
    print(player + " S turn.")
    position =input("choose a position from 1 to 9: \n")
    
    valid = False
    while not valid:

        while position not in ["1" ,"2" ,"3" ,"4" ,"5" ,"6" ,"7" , "8" ,"9"]:
            position =input("choose a position from 1 to 9: \n")

        position=int(position)-1

        if board[position] == "-":
            valid = True
        else:
            print("You can NOT go there.GO again..")

       

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    
    #set up global variable
    global winner
    #check rows
    row_winner=check_rows()

    #check colums:
    column_winner=check_columns()
    #check diagonals
    diagonals_winner=check_diagonals()
    if row_winner:
        #there was a win
        winner=row_winner
    elif column_winner:

        winner =column_winner

    elif diagonals_winner:

        winner = diagonals_winner

    else:
        winner =None

    return



def check_rows():
    #set up global variable
    global game_still_going
    row_1 = board[0] == board[1] ==board[2] != "-"
    row_2 = board[3] == board[4] ==board[5] != "-"
    row_3 = board[6] == board[7] ==board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going=False
    #return the winner (X or O)   
    if row_1:
       return board[0]
    if row_2:
       return board[3]
    if row_3:
       return board[6]
    return

def check_columns():
       #set up global variable
    global game_still_going
    column_1 = board[0] == board[3] ==board[6] != "-"
    column_2 = board[1] == board[4] ==board[7] != "-"
    column_3 = board[2] == board[5] ==board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going=False
    #return the winner (X or O)   
    if column_1:
       return board[0]
    if column_2:
       return board[1]
    if column_3:
       return board[2]
    return

def check_diagonals():
         #set up global variable
    global game_still_going
    diagonals_1 = board[0] == board[4] ==board[8] != "-"
    diagonals_2 = board[6] == board[4] ==board[2] != "-"
    

    if diagonals_1 or diagonals_2 :
        game_still_going=False
    #return the winner (X or O)   
    if diagonals_1:
       return board[0]
    if diagonals_2:
       return board[6]
  
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False


    return


def flip_player():
    #global variables we need
    global current_player
    #if the current player "X" ,then change to the "O"
    if current_player == "X":
        current_player ="O"
    elif current_player =="O": #if the current player "O" ,then change to the "X"
        current_player = "X"

    return

play_game()



