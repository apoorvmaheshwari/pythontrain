import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, threadDelay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.threadDelay = threadDelay
    def run(self):
        print "Starting " + self.name
		print(threadLock.locked())
        threadLock.acquire()
        print_time(self.name, self.threadDelay, 3)
        threadLock.release()

def print_time(threadName, delay, count):
    while count:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        count -= 1

threadLock = threading.Lock()

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
