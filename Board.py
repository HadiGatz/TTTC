class Board:
    board = ""
    def __init__(self):
        self.board = ['-' for i in range(9)]
    
    def print_board(self):
        counter = 0
        for i in range(9):
            print(f"|{self.board[i]}|", end=" ")
            counter += 1
            if (counter >= 3) and (counter % 3 == 0):
                print("\n")
    
    def check_board_state(self):
        # X_WIN - x won
        # O_WIN - o won
        # TIE - tie
        # NO_RESULT - the game is ongoing

        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != '-':
                return f"{self.board[i]}_WIN"
    
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != '-':
                return f"{self.board[i]}_WIN"
    
        if self.board[0] == self.board[4] == self.board[8] != '-':
            return f"{self.board[0]}_WIN"
        if self.board[2] == self.board[4] == self.board[6] != '-':
            return f"{self.board[2]}_WIN"
    
        if '-' not in self.board:
            return "TIE"
    
        return "NO_RESULT"
    
    def set_tile(self, tile_num, tile_type):
        if self.board[tile_num] == '-':
            self.board[tile_num] = tile_type
            return True
        
        return False
