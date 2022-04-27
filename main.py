from Quantum import Client, Server, MiddleMan

host = "127.0.0.1"
serverPort = 12346 # might need to keep changing this if it's being used
clientPort = 12345

def main():
    serverAddress = (host, serverPort)
    clientAddress = (host, clientPort)

    server = Server.Server(serverAddress) # use serverAddress for BOTH if just client/server
    client = Client.Client(clientAddress)
    midman = MiddleMan.MiddleMan(serverAddress, clientAddress)

    client.sendqubits(8) # initial qke exchange
    midman.receiveFromClient() # middleman takes qubits, measures them and takes client's polar
    server.recievequbit()
    server.sendpolar()
    midman.recieveFromServer() # middleman takes server's polar and generates a key
    client.recievepolar()

    client.send('Hello There!') # send from the client
    midman.receiveFromClient() # midman intercepts and passes to server
    message = server.receive()
    print(message) # print what the client recieved

    server.send('General Kenobi') # send from the server
    midman.recieveFromServer() # midman intercepts and passes to client
    message = client.receive()
    print(message) # print what the server recieved
    server.close()

if __name__ == '__main__':
    main()