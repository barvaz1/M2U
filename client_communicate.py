import socket
import threading


class Socket_controller:

    def __init__(self):
        self.my_socket = socket.socket()
        self.my_socket.connect(('127.0.0.1', 80))

        recv_thread = threading.Thread(target=self.recv_data, args=())
        recv_thread.start()

        # send_thread = threading.Thread(target=self.send_data(), args=())
        # send_thread.start()



    def recv_data(self):
        while True:
            print(self.my_socket.recv(1024).decode())

    def send_data(self, data):
        print(1)
        print(data)
        self.my_socket.send(data.encode())


Socket_controller()

