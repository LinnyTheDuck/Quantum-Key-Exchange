from Quantum import Client, Server, MiddleMan

host = "127.0.0.1"
serverPort = 12346 # might need to keep changing this if it's being used
clientPort = 12345

def main():
    serverAddress = (host, serverPort)
    clientAddress = (host, clientPort)

    server = Server.Server(serverAddress) # use serverAddress for BOTH if just client/server
    client = Client.Client(serverAddress)
    midman = MiddleMan.MiddleMan(serverAddress, clientAddress)

    client.send('Hello There!') # send from the client
    message = server.receive()
    print(message) # print what the client recieved

    server.send('General Kenobi') # send from the server
    message = client.receive()
    print(message) # print what the server recieved
    server.close()

if __name__ == '__main__':
    main()