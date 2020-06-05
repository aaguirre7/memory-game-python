#this is my first game
#so cool.. hope you enjoy
#A console based memory game


import os
import random
import time

NUM_ROWS = 2
NUM_COLS = 2

if (NUM_ROWS * NUM_COLS) % 2 != 0:
    raise ValueError("There should be even spots")

HIDDEN_CARD = "#"
EMPTY_SPOT = " "
DELAY = 2 #time the cards are reveled for

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_title():
    print(r""" 
 _______ _______ __   __ _______   _______ _______ 
|       |   _   |  |_|  |       | |       |       |
|    ___|  |_|  |       |    ___| |   _   |    ___|
|   | __|       |       |   |___  |  | |  |   |___ 
|   ||  |       |       |    ___| |  |_|  |    ___|
|   |_| |   _   | ||_|| |   |___  |       |   |    
|_______|_______|__   __|_______|_____________|__  
|  |_|  |       |  |_|  |       |    _ | |  | |  | 
|       |    ___|       |   _   |   | || |  |_|  | 
|       |   |___|       |  | |  |   |_||_|       | 
|       |    ___|       |  |_|  |    __  |_     _| 
| ||_|| |   |___| ||_|| |       |   |  | | |   |   
|_|   |_|_______|_|   |_|_______|___|  |_| |___|
      """)

def print_instructions():
    print("Classic game of memory")
    print("choose two(2) cards that you think match")
    print("find all pairs in the least amount of turns")
    print()


def play_again():
    print()
    print("would you like to play again? (yes or no)?")
    return input().lower().startswith("y")
    


def create_board():
    cards = []
    for offset in range ((NUM_ROWS * NUM_COLS) // 2):
        cards.append(chr(65 + offset))
    
    cards.extend(cards)
    random.shuffle(cards)

    board = []
    for row_num in range(NUM_ROWS):
        new_row = []
        for col_num in range(NUM_COLS):
            new_row.append(cards[row_num * NUM_COLS + col_num])
        board.append(new_row)

    return board


def display_cards(board, visible=None):
    if visible is None:
        visible = []

    row_indices = range(NUM_ROWS)
    col_indices = range(NUM_COLS)
    print("\t", end="")
    for col_index in col_indices:
        print(col_index, end="\t")
    print()
    print("\t", end="")
    for col_index in col_indices:
        print("----", end="\t")
    print()
        
    for row_num in range(NUM_ROWS):
        print(row_indices[row_num], "|\t", end="")
        for col_num in range(NUM_COLS):
            if (row_num, col_num) in visible:
                print(board[row_num][col_num], end="\t")
            elif board[row_num][col_num] == EMPTY_SPOT:
                print(EMPTY_SPOT, end="\t")
            else:
                print(HIDDEN_CARD, end="\t")
        print()
    print()

def validate_user_input(player_choice, board):
    try:
        row, col = player_choice.split()
    except ValueError:
        print("Please enter two(2) number separated by a space")
        return False
    try:
        row = int(row)
        col = int(col)
    except ValueError:
        print("Enter numbers only")
        return False

    if row < 0 or row > NUM_ROWS -1:
        print("the row number must be between 0 and ", NUM_ROWS - 1, ".", sep="")
        return False
    
    if col < 0 or col > NUM_COLS -1:
        print("the column number must be between 0 and ", NUM_COLS - 1, ".", sep="")
        return False
    
    if board[row][col] == EMPTY_SPOT:
        print("that spot is empty")
        return False
        
    return True


def get_player_choices(board):
    player_choices = []
    valid_input = False
    while not valid_input:
        print("Enter the ROW and COLUMN number for your choice of card,")
        player_choice = input("Separeted by a space: ")
        valid_input = validate_user_input(player_choice, board)
    row, col = player_choice.split()
    new_position = (int(row), int(col))
    player_choices.append(new_position)

    valid_input = False
    while not valid_input:
        print("Enter the ROW and COLUMN number for your choice of card,")
        player_choice = input("Separeted by a space: ")
        if validate_user_input(player_choice, board):
            row, col = player_choice.split()
            new_position = (int(row), int(col))
            if new_position not in player_choices:
                player_choices.append(new_position)
                valid_input = True
            else:
                print(" The Cards must be different")
    return player_choices


def player_turn(board, player_score, player_turns):
    clear()
    print_title()
    print("Turns taken:", player_turns)
    print("Current_score:", player_score)
    print()
    display_cards(board)
    player_choices = get_player_choices(board)
    card1_pos, card2_pos = player_choices
    clear()
    print_title()
    print_instructions()
    print()
    print()
    display_cards(board, player_choices)
    
    symbol1 = board[card1_pos[0]][card1_pos[1]]
    symbol2 = board[card2_pos[0]][card2_pos[1]]

    if symbol1 == symbol2:
        board[card1_pos[0]][card1_pos[1]] = EMPTY_SPOT
        board[card2_pos[0]][card2_pos[1]] = EMPTY_SPOT
        player_score += 1
        print("Well done!")
        time.sleep(DELAY)
        return True
    time.sleep(DELAY)
    return False


def main():
    lets_play_again =True
    max_score = NUM_ROWS * NUM_COLS // 2

    while lets_play_again:
        # Initialise values
        board = create_board()
        player_turns = 0
        player_score = 0
        
        #Main Game mechanics
        game_over = False
        while not game_over:
            success = player_turn(board, player_score, player_turns)
            if success:
                player_score += 1
            player_turns += 1

            if player_score >= max_score:
                game_over = True
            

        print()
        print("congratualtions!")
        print("you completed the game in", player_turns, "turns")
        print("your score is ", player_score, ".", sep="")

        if not play_again():
            lets_play_again = False

    print("have a great day")
 

if __name__ =="__main__":
    main()





