from Classes import Client, Server

host = 'localhost'
port = 50003 # might need to keep changing this if it's being used

def main():
    server = Server.Server(host, port)
    client = Client.Client(host, port)

    server.accept() # get the server running
    server.send("Hello World!") # send something to the client
    message = client.receive()
    server.close()

    print(message) # print what the client recieved

if __name__ == '__main__':
    main()