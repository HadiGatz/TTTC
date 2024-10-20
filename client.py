import socket
from Board import *
from TTTManager import *
import login_client
import pickle

board = Board()
manager = TTTManager(board)

HOST = '192.168.68.104'
PORT = 5555

HOST_LOGIN = '192.168.68.104'
PORT = 5557
client = socket.socket()
    
def send_move_to_server(client, tile_type):
    chosen_tile = manager.handle_user_turn(tile_type)
    data = pickle.dumps((chosen_tile, tile_type))
    client.send(data)

def connect_to_server():
    client.connect((HOST, PORT))


while True:
    login_client.handle_login(client)
    random_id = client.recv(1024).decode()
    
    ready = input("\nAre you ready to play? [Y/N]: ").lower()
    if ready == 'y':
        connect_to_server()
        data = client.recv(1024).decode()
        tile_type = 'X' if data == "FIRST" else 'O'
        
        while True:
            command = client.recv(1024).decode()

            current_board = client.recv(1024).decode()
            print(current_board)

            if command == "MOVE":
                print("\nYour move\n")
                send_move_to_server(client, tile_type)
            else:
                print("\nWaiting for your opponent's move...\n")

            current_board = client.recv(1024).decode()
            print(current_board)

            current_game_state = client.recv(1024).decode()
            if current_game_state != "NO_RESULT":
                break
    
    else:
        break



