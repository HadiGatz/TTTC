import sqlite3
import hashlib
import socket
import json
import random
import select
import threading

HOST = ''
PORT = 5557
server = socket.socket()
server.bind((HOST, PORT))

connection_to_game_server = socket.socket()
connection_to_game_server.connect(('192.168.68.104', 5556))


con = sqlite3.connect("userdata.db")
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users
            (username text PRIMARY KEY, password text)''')

def generate_random_number():
    return random.randint(1, 10000000000000)

def send_random_id_to_server_and_client(client, game_server, id):
    client.send((str(id)).encode())
    game_server.send((str(id)).encode())

    
def check_username(username):
    return len(username) >= 1 and len(username) <= 12

def add_user(username, password):
    cur.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, hash_password(password)))
    con.commit()

def hash_password(password):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode())
    return sha256_hash.hexdigest()

def check_if_username_in_database(username):
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cur.fetchone():
        return True
    return False

def check_for_users_password(username, password):
    hashed_password = hash_password(password)
    cur.execute("SELECT password FROM users WHERE username = ?", (username,))
    actual_password = cur.fetchone()
    return actual_password[0] == hashed_password

def retrieve_user_data_from_json(data):
    user_data_json = json.loads(data)
    username, password = user_data_json["username"], user_data_json["password"]
    return (username, password)

def handle_login(client):
    logged_in = False
    while not logged_in:
        data = client.recv(1024).decode()
        username, password = retrieve_user_data_from_json(data)

        if check_if_username_in_database(username):
            if check_for_users_password(username, password):
                client.send("SUCCESS".encode())
            else:
                client.send("PASSWORD".encode())
        else:
            client.send("USERNAME".encode())
            username = client.recv(1024).decode()
            if check_username(username):
                client.send("SUCCESS".encode())
                password = client.recv(1024).decode()

                add_user(username, hash_password(password))
                random_id = generate_random_number()
                send_random_id_to_server_and_client(client, connection_to_game_server, random_id)

def login_server():
    # client_sockets = []

    # while True:
    #     rlist, wlist, xlist = select.select([server] + client_sockets, [], [])

    #     for socket in rlist:
    #         if socket == server:
    #             client, address = server.accept()
    #             handle_login(client)
            
    #         else:
    while True:
        server.listen()
        client, address = server.accept()
        print(f"[CONNECTION] {address}")

        login_proccess = threading.Thread(target=handle_login, args=(client,))
        login_proccess.start()

login_server()


                
