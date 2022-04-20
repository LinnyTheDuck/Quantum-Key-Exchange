import socket, sys

run = True

def init():
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # setting up TCP
    serverAddr = ('localhost', 88) # addr is a port 88
    tcpSocket.bind(serverAddr) # bind socket to server address
    tcpSocket.listen(1) # LISTENNN TO THE SOUND OF THE PORTTT

    while run:
        print("Waiting for connection")
        connection, client = tcpSocket.accept()
    
        try:
            print("Connected to client IP: {}".format(client))
            
            while True:
                data = connection.recv(128) # 128 bytes at a time
                print("Received data: {}".format(data))
    
                if not data:
                    break # as long as client is sending something
    
        finally:
            connection.close()

def send(message):
    print(message) # server sends shit to the client, how do we do that huh

def close():
    run = False # destroy's the main while loop ??