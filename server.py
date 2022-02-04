import socket
import select

MAX_MSG_LENGTH = 1024
SERVER_PORT = 80
SERVER_IP = "0.0.0.0"

def main():

    # open socket with client
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen()

    # lst of all the sockets
    client_sockets = {}
    messages_to_send = []

    # handle requests until user asks to exit
    done = False
    while not done:

        # create list of all the sockets
        client_sockets_lst = list(client_sockets.keys())
        left_the_chats = []
        join_the_chats = []
        # socket before connection
        r_list, w_list, x_list = select.select([server_socket] + client_sockets_lst, client_sockets_lst, [])

        for current_socket in r_list:

            # new client?
            if current_socket is server_socket:
                connection, client_address = current_socket.accept()
                print("New client joined!", client_address)
                # connection: room, name, new sockets, new msg
                client_sockets[connection] = [None]

            else:
                # get data from existing client
                print("Data from existing client")
                data = current_socket.recv(MAX_MSG_LENGTH).decode()

                # empty data?
                if data == "":
                    print("Connection closed", )
                    del client_sockets[current_socket]
                    current_socket.close()

                # new cmd?
                else:

                    messages_to_send.append((current_socket, "Data: " + data))

        if messages_to_send:
            print(1)
            print(messages_to_send)
        for message in messages_to_send:
            current_socket, data = message
            if current_socket in w_list:
                current_socket.send(data.encode())
            messages_to_send.remove(message)


if __name__ == '__main__':
    main()