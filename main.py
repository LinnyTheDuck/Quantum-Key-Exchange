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
    print("Client Sent Message: Hello There!")
    len = client.length() # passing the length
    midman.setlen(len)
    midman.receiveFromClient() # midman intercepts and passes to server
    server.setlen(len)
    message = server.receive()
    print("Server Recieved Message: "+message) # print what the client recieved

    '''server.send('General Kenobi') # send from the server
    len = server.length() # passing the length
    midman.setlen(len)
    midman.recieveFromServer() # midman intercepts and passes to client
    client.setlen(len)
    message = client.receive()
    print(message) # print what the server recieved'''

    server.close()

if __name__ == '__main__':
    main()