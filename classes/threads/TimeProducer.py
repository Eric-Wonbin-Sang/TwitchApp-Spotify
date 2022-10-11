import time
import threading

from queue import Queue


class TimeProducer(threading.Thread):

    def __init__(self, thread_id, name, queue):
        threading.Thread.__init__(self)

        self.thread_id = thread_id
        self.name = name
        self.queue = queue

    def run(self):
        while True:
            time.sleep(1)
            threading.Event()