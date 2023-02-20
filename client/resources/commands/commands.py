class Commands:
    def __init__(self, status, client):
        self.status = status
        self.client = client

    def commands(self):
        while True:
            command_request = input("Enter command: ")
            if command_request == "available":
                print(self.status.format_time(
                    self.status.available, "Available"))
            elif command_request == "busy":
                print(self.status.format_time(self.status.busy, "Busy"))
            elif command_request == "dnd":
                print(self.status.format_time(
                    self.status.do_not_disdurb, "DoNotDisturb"))
            elif command_request == "avay":
                print(self.status.format_time(self.status.away, "away"))
            elif command_request == "brb":
                print(self.status.format_time(
                    self.status.be_right_back, "BeRightBack"))
            elif command_request == "call":
                print(self.status.format_time(self.status.on_the_phone, "call"))
            elif command_request == "all":
                print(self.status.format_time(
                    self.status.available, "Available"))
                print(self.status.format_time(self.status.busy, "Busy"))
                print(self.status.format_time(self.status.away, "Away"))
                print(self.status.format_time(
                    self.status.do_not_disdurb, "DoNotDisturb"))
                print(self.status.format_time(
                    self.status.be_right_back, "BeRightBack"))
                print(self.status.format_time(
                    self.status.on_the_phone, "InCall"))
            elif command_request == "help":
                print("Show all: all")
                print("Show available: available")
                print("Show busy: busy")
                print("Show away: away")
                print("Show do not disturb: dnd")
                print("Show be right back: brb")
                print("Show in call: call")

    def light_commands(self):
        while True:
            if self.status.get_status() == "Available":
                self.client.send("1")
            elif self.status.get_status() != "Available":
                self.client.send("0")
