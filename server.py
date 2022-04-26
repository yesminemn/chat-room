import threading
import socket
import sys 
import argparse
import time

#TODO: Implement all code for your server here

# Use sys.stdout.flush() after print statemtents



#creating the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#parsing arguments from terminal
parser = argparse.ArgumentParser(description='Socket connection arguments')
parser.add_argument('-start', '--start', action='store_true')
parser.add_argument('-port', '--port', type=int, default=8080, help='port')
parser.add_argument('-passcode', '--passcode') 
options = parser.parse_args()

server.bind(("127.0.0.1", options.port))
server.listen(5)
print('Server started on port %i. Accepting connections' % (options.port))
sys.stdout.flush()


clients_sockets = []
users = []

#broadcasting messages
def broadcast(message,sender):
    for client in clients_sockets:
        if client != sender: #send messages to everyone but the sender
            client.send(message)


#function to handle clients'connections and recieve messages
def handle_client(client):
    while True:
        try:
            message = client.recv(100)
            message_split = message.decode('utf-8').split(': ')
            if message_split[1] == ":Exit": #user leaving chat
                broadcast(f'{user} left the chatroom'.encode('utf-8'),client)
                print(f'{user} left the chatroom')
                sys.stdout.flush()
                index = clients_sockets.index(client)
                clients_sockets.remove(client)
                client.close()
                user = users[index]
                users.remove(user)
                break
            else:
                broadcast(message,client)
                print(message.decode('utf-8'))
                sys.stdout.flush()
        except:
            index = clients_sockets.index(client)
            clients_sockets.remove(client)
            client.close()
            user = users[index]
            broadcast(f'{user} left the chatroom'.encode('utf-8'),client)
            users.remove(user)
            break


#function to receive the clients connection
def receive():
    while True:
        #establishing connection with a new client
        client, address = server.accept()
        sys.stdout.flush()
        #getting username and password
        new_user = client.recv(100).decode('utf-8').split(':')
        username = new_user[0]
        password = new_user[1]

        #checking password
        if password != options.passcode:
            client.send('Incorrect passcode'.encode('utf-8'))
            time.sleep(3)
            client.close()
            continue
        #user joined the chatroom    
        users.append(username)
        clients_sockets.append(client)
        client.send(f'Connected to 127.0.0.1 on port {options.port}'.encode('utf-8'))
        print(f'{username} joined the chatroom')
        sys.stdout.flush()
        broadcast(f'{username} joined the chatroom'.encode('utf-8'),client)
        #start a thread for the new client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.join()
        thread.start()


if __name__ == "__main__":
    receive()