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
    board[index] = 'X'
    button_vars[index].set(board[index])

counter = 0
for row in range(3):
    for col in range(3):
        button_vars[counter].set(board[counter])

        button = tk.Button(root, textvariable=button_vars[counter], width=button_width//10, height=button_height//20)

        button.config(command=lambda index=counter: on_button_click(index))

        button.grid(row=row, column=col, sticky="nsew")

        counter += 1

for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
