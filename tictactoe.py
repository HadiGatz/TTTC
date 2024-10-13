import random
from Board import *

board = Board()
number_of_rounds = 0

def handle_computer_turn():
    while True:
        random_tile = random.randint(0,8)
        if board.set_tile(random_tile, 'O'):
            break


def handle_user_turn():
    while True:
        tile = int(input("Enter your tile: "))
        if tile >= 0 and tile <= 8 and board.set_tile(tile, 'X'):
            break

def handle_game_ending(result):
    if result == "TIE":
        print("The game has ended with a TIE")
    
    else:
        print(result.replace("_", " "))

def check_game_over():
    current_result = board.check_board_state()
    if current_result != "NO_RESULT":
        board.print_board()
        handle_game_ending(current_result)
        return True
    return False

def game_logic(number_of_rounds):    
    while True:
        board.print_board()  

        handle_user_turn()

        number_of_rounds += 1
        
        if check_game_over():
            break

        handle_computer_turn()

        if check_game_over():
            break

if __name__ == "__main__":
    game_logic(number_of_rounds)


        
        


