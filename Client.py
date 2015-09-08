import socket

s = socket.socket()
PORT = 7273

# IP and PORT should be taken from config file or from the user
s.connect(("192.168.10.125", PORT))


while True:
    message = input("Enter your message: ")
    s.send(message.encode())



