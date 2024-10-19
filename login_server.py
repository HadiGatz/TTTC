import sqlite3
import hashlib
import socket
import json

HOST = ''
PORT = 5556
server = socket.socket()
server.bind((HOST, PORT))

con = sqlite3.connect("userdata.db")
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users
            (username text PRIMARY KEY, password text)''')

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
                break

server.listen()
client, address = server.accept()
handle_login(client)
client.close()
