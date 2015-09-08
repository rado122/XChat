import socket
import threading

RECV_BUFFER = 4096


class ReceiveMessageProcess(threading.Thread):
    def __int__(self, server_socket):
        threading.Thread.__init__(self, group=None)
        self.server_socket = server_socket
        self.daemon = True

    def run(self):
        while 1:
            message = self.server_socket.recv()
            print(message.decode())


class SendMessageProcess(threading.Thread):
    def __init__(self, server_socket):
        threading.Thread.__init__(self, group=None)
        self.server_socket = server_socket
        self.daemon = True

    def run(self):
        while 1:
            message = input("Enter your message: ")
            self.server_socket.send(message.encode())


PORT = 7273

if __name__ == "__main__":
    s = socket.socket()
    # IP and PORT should be taken from config file or from the user
    s.connect(("192.168.10.125", PORT))
    message_sender_process = SendMessageProcess(s)
    message_receiver_process = ReceiveMessageProcess(s)

    message_receiver_process.start()
    message_sender_process.start()





