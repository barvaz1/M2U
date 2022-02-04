import socket
import threading


class Socket_controller:

    def __init__(self):
        self.my_socket = socket.socket()
        self.my_socket.connect(('127.0.0.1', 80))

        receve_thread = threading.Thread(target=self.receve_data, args=())
        receve_thread.start()

        send_thread = threading.Thread(target=self.send_data(), args=())
        send_thread.start()

    def receve_data(self):
        while True:
            print(self.my_socket.recv(1024).decode())

    def send_data(self):
        while True:
            str = input("pls enter a string: ")
            self.my_socket.send(str.encode())

Socket_controller()
