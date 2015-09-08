import socket
import threading


# Not implemented yet
def send_message(message, clients_list):
    # Print is only for test purposes
    print(message.decode())


# Client Worker process
class ClientWorker(threading.Thread):
    def __init__(self, client_socket, clients_list):
        threading.Thread.__init__(self)
        self.daemon = True
        self.clients_list = clients_list
        self.client_socket = client_socket

    def run(self):
        while 1:
            message = self.client_socket.recv(RECV_BUFFER)
            send_message(message, self.clients_list)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 7273  # Later should be taken from config file
RECV_BUFFER = 4096
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(5)
connected_clients = []  # List of connected clients

if __name__ == "__main__":
    while True:
        c, address = server_socket.accept()
        # If it is an already connected client continue listening for connections
        if c in connected_clients:
            continue
        # If it is a new connection add it to connected clients list and start new process for it
        else:
            connected_clients.append(c)
            worker = ClientWorker(c, connected_clients)
            worker.start()





