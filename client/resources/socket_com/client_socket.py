import socket


class ClientSocket:
    def __init__(self, header, port, server, text_foramt, disconnect_message):
        self.header = header
        self.port = port
        self.server = server
        self.text_format = text_foramt
        self.disconnect_message = disconnect_message
        self.address = (server, port)
        self.connect()

    def connect(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(self.address)
        except:
            print("Failed to connect. Please try again")

    def send(self, msg):
        message = msg.encode(self.text_format)
        msg_length = len(message)
        send_lenght = str(msg_length).encode(self.text_format)
        send_lenght += b' '*(self.header - len(send_lenght))
        self.client.send(send_lenght)
        self.client.send(message)

    def close_connection(self):
        self.client.close()
