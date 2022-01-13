# Assignment - W02 Prove: Developer - Solo Code Submission
# Tic-tac-toe
# Author - Robert Lowry

board_grid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def main():
    print("""
Welcome to Tic-Tac-Toe

In this game player 1 controls x's and
player 2 controls o's. Each player gets 
a turn to choose which space to place
either an x or an o, whichever they
control. The first player to get 3 in a
row wins the game.
""")
    player_one_name = input("What is player 1's name? ")
    player_two_name = input("What is player 2's name? ")

    print('''
To pick a space type the number for the
space you want to place your x or o and
hit enter. Each player will take turns
picking spaces. The game will end when
one player has an entire row, column,
or diagonal. The game will also end
if the board is completely filled up.
''')

    input('Press enter to begin.')
    # starting the board and setting player turn
    # to 2 so that it switches to 1 when the game
    # begins.
    reset_board()
    current_player_turn = 2

    # This will run until the loop is broken when
    # the players choose to end the game.
    while True:
        
        # These if and elif statement change which
        # players turn it is.
        if current_player_turn == 1:
            current_player_name = player_two_name
            current_player_piece = "o"
            current_player_turn = 2
        elif current_player_turn == 2:
            current_player_name = player_one_name
            current_player_piece = "x"
            current_player_turn = 1
        print_board()
        # This is the start of the players turn. The player
        # will type a number of a space and place their piece
        # there. If the number entered is either not on the
        # board or already taken it will be rejected and the
        # loop will make the player pick a new number.
        while True:
            space_number = int(input(f"Where would you like to go {current_player_name}? "))
            if is_number_valid(space_number):
                board_grid[space_number] = current_player_piece
                break
            print("Space number is unavailable. Pick another space.")
        # These if and elif statements determine if the game is over.
        # If a player has won, or the game ends in a draw they will
        # be asked it they would like to play again. otherwise the 
        # loop will continue and the next player will get a turn.
        if three_in_a_row(current_player_piece):
            print(f"Congratulations {current_player_name}! you have won!")
        elif is_draw():
            print("It's a draw!")
        elif three_in_a_row(current_player_piece) == False:
            continue
        
        to_play_again = input("Would you like to play again? (Y or N) ")
        if to_play_again.lower() == "y":
            reset_board()
            continue
        break

    

def print_board():
    """This function shows the board in its current
        state to the players."""
    print(f"""
{board_grid[1]}|{board_grid[2]}|{board_grid[3]}
-+-+-
{board_grid[4]}|{board_grid[5]}|{board_grid[6]}
-+-+-
{board_grid[7]}|{board_grid[8]}|{board_grid[9]}
""")
    
def player_has_row(player):
    """This functions takes one argument, player, 
        and determines if the have a row filled
        with their piece."""
    if board_grid[1] == player and board_grid[2] == player and board_grid[3] == player:
        return True
    if board_grid[4] == player and board_grid[5] == player and board_grid[6] == player:
        return True
    if board_grid[7] == player and board_grid[8] == player and board_grid[9] == player:
        return True
    return False

def player_has_column(player):
    """This functions takes one argument, player, 
        and determines if the have a column filled
        with their piece."""
    if board_grid[1] == player and board_grid[4] == player and board_grid[7] == player:
        return True
    if board_grid[2] == player and board_grid[5] == player and board_grid[8] == player:
        return True
    if board_grid[3] == player and board_grid[6] == player and board_grid[9] == player:
        return True
    return False

def player_has_diagonal(player):
    """This functions takes one argument, player, 
        and determines if the have a diagonal
        filled with their piece."""
    if board_grid[1] == player and board_grid[5] == player and board_grid[9] == player:
        return True
    if board_grid[7] == player and board_grid[5] == player and board_grid[3] == player:
        return True
    return False

def reset_board():
    
    board_grid[1] = 1
    board_grid[2] = 2
    board_grid[3] = 3
    board_grid[4] = 4
    board_grid[5] = 5
    board_grid[6] = 6
    board_grid[7] = 7
    board_grid[8] = 8
    board_grid[9] = 9

def is_number_valid(number):
    if number > 9:
        return False
    if number < 1:
        return False
    # if the board space has already been taken
    # return false
    if board_grid[number] != number:
        return False
    return True

def three_in_a_row(player_piece):
    if player_has_row(player_piece) or player_has_column(player_piece) or player_has_diagonal(player_piece):
        return True
    return False

def is_draw():
    for space in board_grid:
        if space == 0:
            continue
        if type(space) == int:
            return False
    return True

if __name__ == "__main__":
    main()
