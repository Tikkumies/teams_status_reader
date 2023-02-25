import RPi.GPIO as GPIO
import socket
import threading
from get_ip import get_network_adapters, parse_wlan_from_ifconfig

relay1 = 37
relay2 = 38
relay3 = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)

GPIO.output(relay1, GPIO.LOW)
GPIO.output(relay2, GPIO.LOW)
GPIO.output(relay3, GPIO.LOW)


HEADER = 16
PORT = 5050
SERVER = parse_wlan_from_ifconfig(get_network_adapters())
print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            if msg == "1":
                GPIO.output(relay1, GPIO.HIGH)
            elif msg == "0":
                GPIO.output(relay1, GPIO.LOW)

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

        

if __name__ == "__main__":
    print("[STARTING] server is starting...")
    start()





