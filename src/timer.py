from threading import Thread
import threading
import time
# from tkinter import Event

class my_thread(Thread):
    def __init__(self, name, time):
        Thread.__init__(self)
        self.time = time
        self.name = name
        self.cur_time = 0

    def run(self):
       # self.cur_thread.start()
        for i in range(self.time):
            print(threading.currentThread().getName() + ": " + str(i))
            time.sleep(1)
            self.cur_time = i + 1
        print("finito")

    def get_time(self):
        #print(self._running)
        return self.cur_time

    