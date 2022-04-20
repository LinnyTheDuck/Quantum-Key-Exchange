from Classes import Client, Server

def main():
    client: Client = Client()
    server: Server = Server()

    server.init() # get the server running
    # I think the server needs to connect ot the client
    server.send("Hello World!") # send something to the client
