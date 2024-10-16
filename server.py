import socket
import threading
import random
import pickle
from TTTManager import *
from Board import *

HOST = ''
PORT = 5555
server = socket.socket()
server.bind((HOST, PORT))

active_players = []

def send_board_to_players(board, player_1, player_2):
    current_board = board.get_board()
    player_1.send(current_board.encode())
    player_2.send(current_board.encode())

def run_game(player_1, player_2):
    board = Board()

    current_player = random.choice([player_1, player_2])
    opponent = player_1 if current_player is player_2 else player_2
    current_player.send("FIRST".encode())
    opponent.send("SECOND".encode())

    if board.check_board_state() == "NO_RESULT":
        while True:
            current_player.send("MOVE")
            current_player.send("WAIT_MOVE")
            send_board_to_players(board, player_1, player_2)

            data = current_player.recv(1024)
            tile, tile_type = pickle.loads(data)
        
            if board.check_tile(tile):
                board.set_tile(tile, tile_type)
            else:
                break #TODO: add error handling - disconnect client if false
            
            send_board_to_players(board, player_1, player_2)

            current_player.send(board.check_board_state().encode())
            opponent.send(board.check_board_state().encode())

            current_player, opponent = opponent, current_player
    else:
        return


def main_game_server():
    while True:
        server.listen()

        client_socket, client_address = server.accept()
        active_players.append(client_socket)

        if len(active_players) > 1:
            game = threading.Thread(target=run_game, args=(active_players[0], active_players[1]))
            active_players = active_players[2:]

            game.start()


    