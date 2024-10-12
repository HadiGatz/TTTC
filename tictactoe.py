import random

board = ['-' for i in range(9)]
number_of_rounds = 0

def handle_computer_turn():
    while True:
        random_tile = random.randint(0,8)
        if board[random_tile] == '-':
            board[random_tile] = 'O'
            break

def print_board():
    counter = 0
    for i in range(9):
        print(f"|{board[i]}|", end=" ")
        counter += 1
        if (counter >= 3) and (counter % 3 == 0):
            print("\n")

def handle_user_turn():
    while True:
        tile = int(input("Enter your tile: "))
        if board[tile] == '-' and tile >= 0 and tile <= 8:
            board[tile] = 'X'
            break



def check_board_state(board):
    # X_WIN - x won
    # O_WIN - o won
    # TIE - tie
    # NO_RESULT - the game is ongoing

    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != '-':
            return f"{board[i]}_WIN"
    
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != '-':
            return f"{board[i]}_WIN"
    
    if board[0] == board[4] == board[8] != '-':
        return f"{board[0]}_WIN"
    if board[2] == board[4] == board[6] != '-':
        return f"{board[2]}_WIN"
    
    if '-' not in board:
        return "TIE"
    
    return "NO_RESULT"

def handle_game_ending(result):
    if result == "TIE":
        print("The game has ended with a TIE")
    
    else:
        print(result.replace("_", " "))

def check_game_over():
    current_result = check_board_state(board)
    if current_result != "NO_RESULT":
        print_board()
        handle_game_ending(current_result)
        return True
    return False

def game_logic(number_of_rounds):    
    while True:
        print_board()  

        handle_user_turn()

        number_of_rounds += 1
        
        if check_game_over():
            break

        handle_computer_turn()

        if check_game_over():
            break

if __name__ == "__main__":
    game_logic(number_of_rounds)


        
        


