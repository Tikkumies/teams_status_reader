from .socket_com import client_socket
from .teams_status import teams_status
from .commands import commands
import time
import schedule
import threading
import os


def main():
    user = os.getlogin()
    log = "C:\\Users\\" + user + "\\AppData\\Roaming\\Microsoft\\Teams\\logs.txt"
    client = client_socket.ClientSocket(
        16, 5050, "192.168.0.49", "utf-8", "!DISCONNECT")
    status = teams_status.Status(log)
    command = commands.Commands(status, client)
    start = time.time()
    schedule.every().minute.do(lambda: status.count())
    scheduler_thread = threading.Thread(target=status.run_scheduler)
    status_command_thread = threading.Thread(target=command.commands)
    light_command_thread = threading.Thread(target=command.light_commands)
    scheduler_thread.start()
    status_command_thread.start()
    light_command_thread.start()


if __name__ == "__main__":
    main()
