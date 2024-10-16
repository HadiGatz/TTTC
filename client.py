import socket
from Board import *
from TTTManager import *
import pickle

board = Board()
manager = TTTManager(board)

HOST = '192.168.68.104'
PORT = 5555
client = socket.socket()
client.connect((HOST, PORT))
    
data = client.recv(1024).decode()
tile_type = 'X' if data == "FIRST" else 'O'

def send_move_to_server(client, tile_type):
    chosen_tile = manager.handle_user_turn(tile_type)
    data = pickle.dumps((chosen_tile, tile_type))
    client.send(data)

while True:
    command = client.recv(1024).decode()
    current_board = client.recv(1024).decode()
    print(current_board)

    if command == "MOVE":
        print("\nYour move")
        send_move_to_server()
    else:
        print("\nWaiting for your opponent's move...")

    current_board = client.recv(1024).decode()
    print(current_board)

    current_game_state = client.recv(1024).decode()
    if current_game_state != "NO_RESULT":
        print(current_game_state.replace("_", " "))
        break



