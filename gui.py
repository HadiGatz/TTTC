import tkinter as tk
from tictactoe import *

number_of_rounds = 0

root = tk.Tk()
root.title("TicTacToe")
root.geometry("600x600")

button_width = 200
button_height = 200

button_vars = [tk.StringVar() for _ in range(9)]

def update_buttons():
    for i in range(9):
        button_vars[i].set(board[i])

def on_button_click(index):

    if board[index] == '-':  
        handle_user_turn(index)
        update_buttons()  
        
        if check_game_over():  
            return

        handle_computer_turn()
        update_buttons()  
        check_game_over()  

counter = 0
for row in range(3):
    for col in range(3):
        button_vars[counter].set(board[counter])  

        button = tk.Button(root, textvariable=button_vars[counter], width=button_width // 10, height=button_height // 20)
        button.config(command=lambda index=counter: on_button_click(index))
        button.grid(row=row, column=col, sticky="nsew")

        counter += 1

for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
