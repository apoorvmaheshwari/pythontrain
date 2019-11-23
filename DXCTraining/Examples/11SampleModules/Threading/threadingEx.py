import threading, time,sys
class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.delay, 5)
        print("Exiting " + self.name)

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-3", 3)
thread3.setDaemon(True)
thread1.start()
thread2.start()
thread3.start()
print("Number of active threads are: ",threading.activeCount())
print("Current Thread : ",threading.currentThread())
print("Exiting ",threading.currentThread().getName())





'''
thread3.setDaemon(True)
thread1.start()
thread2.start()
thread3.start()
thread3.join()
print("Number of active threads are: ",threading.activeCount())
print("Current Thread : ",threading.currentThread())
print("Exiting ",threading.currentThread().getName())

'''
#thread2.setDaemon(True)
#thread3.setDaemon(True)
#$thread1.setDaemon(True)
# Start new Threads





