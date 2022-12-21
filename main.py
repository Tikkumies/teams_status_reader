import time
import schedule
import threading
import os

class Status:
    def __init__(self, log):
        self.log = log
        self.available = 0
        self.busy = 0
        self.do_not_disdurb = 0
        self.be_right_back = 0
        self.appear_away = 0
        self.appear_offline = 0
        self.on_the_phone = 0
        self.away = 0

    def get_status(self):
        with open(self.log, encoding='utf-8') as log:
            text = (log.read())
            status1 = text.rpartition("current state: ")
            status2 = status1[2].partition("-> ")
            status3 = status2[2]. partition(")")
        return status3[0]

    def count_status(self):
        status = self.get_status()
        match status:
            case "Available":
                self.available += 1
            case "Busy":
                self.busy += 1
            case "DoNotDisturb":
                self.do_not_disdurb += 1
            case "BeRightBack":
                self.be_right_back += 1
            case "OnThePhone":
                self.on_the_phone += 1
            case "Away":
                self.away += 1

    def format_time(self, minutes, text):
        hours = int(minutes/60)
        mins = minutes % 60
        return text + ": " + str(hours) + "h " + str(mins) + "min"

    def commands(self):
        while True:
            command_request = input("Enter command: ")
            if command_request == "available":
                print(self.format_time(self.available, "Available"))
            elif command_request == "busy":
                print(self.format_time(self.busy, "Busy"))
            elif command_request == "dnd":
                print(self.format_time(self.do_not_disdurb, "DoNotDisturb"))
            elif command_request == "avay":
                print(self.format_time(self.away, "away"))
            elif command_request == "brb":
                print(self.format_time(self.be_right_back, "BeRightBack"))
            elif command_request == "call":
                print(self.format_time(self.on_the_phone, "call"))
            elif command_request == "all":
                print(self.format_time(self.available, "Available"))
                print(self.format_time(self.busy, "Busy"))
                print(self.format_time(self.away, "Away"))
                print(self.format_time(self.do_not_disdurb, "DoNotDisturb"))
                print(self.format_time(self.be_right_back, "BeRightBack"))
                print(self.format_time(self.on_the_phone, "InCall"))
            elif command_request == "help":
                print("Show all: all")
                print("Show available: available")
                print("Show busy: busy")
                print("Show away: away")
                print("Show do not disturb: dnd")
                print("Show be right back: brb")
                print("Show in call: call")
            else: pass
        

def count():
    status.count_status()

def run_scheduler():
    while True:
        schedule.run_pending()

if __name__ == "__main__":
    user = os.getlogin()
    log = "C:\\Users\\" + user  + "\\AppData\\Roaming\\Microsoft\\Teams\\logs.txt"
    status = Status(log)
    start = time.time()
    schedule.every().minute.do(lambda: count())
    thread = threading.Thread(target=run_scheduler)
    thread.start()
    status.commands()






        


