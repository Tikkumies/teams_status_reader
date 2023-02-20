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

    def count(self):
        self.count_status()

    def run_scheduler(self):
        while True:
            schedule.run_pending()
