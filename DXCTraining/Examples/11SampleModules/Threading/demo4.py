from threading import Thread,activeCount,currentThread
from time import sleep
class Mythread(Thread):
	def __init__(self,name,delay):
		super().__init__()
		self.name=name
		self.delay=delay
	def run(self):
		for i in range(1,6):
			print(str(i)+self.name)
			sleep(self.delay)
		print('Exiting Thread_'+self.name)
		
		
t1 = Mythread('Sachin',1)
t2 = Mythread('Rahul',2)
t2.setDaemon(True)
#t1.setDaemon(True)
t1.start()
t2.start()
print('Exiting MainThread!!!')