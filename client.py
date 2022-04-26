import threading
import socket
import errno
import argparse
import time
from datetime import datetime
from datetime import timedelta
import sys

#TODO: Implement a client that connects to your server to chat with other clients here

# Use sys.stdout.flush() after print statemtents


#creating the socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#parsing args from terminal
parser = argparse.ArgumentParser(description='Socket connection arguments')
parser.add_argument('-join', '--client', action='store_true')
parser.add_argument('-host', '--host') 
parser.add_argument('-port', '--port', type=int)
parser.add_argument('-username', '--username') 
parser.add_argument('-passcode', '--passcode') 
options = parser.parse_args()

#use arguments to connect
HOST = options.host
PORT = options.port
my_username = options.username
password = options.passcode

# Connect to the given ip and port
client.connect((HOST, PORT))

#Send username and password
client.send(f'{my_username}:{password}'.encode('utf-8'))

#actively waiting for messages
def client_receive():
    while True:
        try:
            message = client.recv(100).decode('utf-8')
            if message == 'Incorrect passcode':
                print(message)
                sys.stdout.flush()
                client.close()
                break
            print(message)
            sys.stdout.flush()
        except:
            print('Error!')
            sys.stdout.flush()
            client.close()
            break


#actively sending input messages from user
def client_send():
    while True:
        message = f'{my_username}: ' + input()
       
        message = message.replace(':)','[feeling happy]')
        message = message.replace(':(','[feeling sad]')

        current_time = datetime.now()
        hours_added = timedelta(hours = 1)
        future_time = current_time + hours_added

        message = message.replace(':mytime',current_time.strftime("%H:%M:%S"))
        message = message.replace(':+1hr',future_time.strftime("%H:%M:%S"))
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()

if __name__ == "__main__":
    pass