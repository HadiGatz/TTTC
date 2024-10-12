import tkinter as tk
import tictactoe
from tictactoe import board

root = tk.Tk()
root.title("TicTacToe")
root.geometry("600x600")

button_width = 200
button_height = 200
button_vars = [tk.StringVar() for _ in range(9)]

def on_button_click(index):
    # Set the user's move and update the board
    if board[index] == '-':  # Ensure the tile is empty before placing 'X'
        tictactoe.handle_user_turn()  # Call the user turn function
        button_vars[index].set(board[index])  # Update the button to show 'X'
        
        if tictactoe.check_game_over():  # Check for game over after user turn
            return
        
        tictactoe.handle_computer_turn()  # Handle the computer's turn
        # Update GUI to reflect computer's move
        for i in range(9):
            if board[i] == 'O':
                button_vars[i].set(board[i])  # Update button to show 'O'
        
        tictactoe.check_game_over()  # Check for game over after computer turn

# Initialize buttons
counter = 0
for row in range(3):
    for col in range(3):
        button_vars[counter].set(board[counter])
        button = tk.Button(root, textvariable=button_vars[counter], width=button_width//10, height=button_height//20)
        button.config(command=lambda index=counter: on_button_click(index))
        button.grid(row=row, column=col, sticky="nsew")
        counter += 1

# Configure grid
for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
