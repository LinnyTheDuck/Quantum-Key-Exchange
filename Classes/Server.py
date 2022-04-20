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

def send(message): # i stole some code... need to clean this up
    # take the server name and port name
    host = 'local host'
    port = 5000
    
    # create a socket at server side
    # using TCP / IP protocol
    s = socket.socket(socket.AF_INET,
                    socket.SOCK_STREAM)
    
    # bind the socket with server
    # and port number
    s.bind(('', port))
    
    # allow maximum 1 connection to
    # the socket
    s.listen(1)
    
    # wait till a client accept
    # connection
    c, addr = s.accept()
    
    # display client address
    print("CONNECTION FROM:", str(addr))
    
    # send message to the client after
    # encoding into binary string
    c.send(b"HELLO, How are you ? \
        Welcome to Akash hacking World")
    
    msg = "Bye.............."
    c.send(msg.encode())
    
    # disconnect the server
    c.close()

def close():
    run = False # destroy's the main while loop ??