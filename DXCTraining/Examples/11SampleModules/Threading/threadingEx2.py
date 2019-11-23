import threading, time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
start=time.time()
# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(2, "Thread-3", 1)
#setDaemon()
#thread1.setDaemon(True)
#thread2.setDaemon(True)
#thread3.setDaemon(True)
# Start new Threads
thread1.start()
thread2.start()
thread3.start()
while(threading.activeCount()>1):
    #print("Number of active threads are: ",threading.activeCount())
   time.sleep(1)
end=time.time()-start
print("Time taken: ",end)
print("Exiting ",threading.currentThread().getName())








