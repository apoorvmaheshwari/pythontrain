from threading import Thread , BoundedSemaphore
from time import sleep
sema=BoundedSemaphore(5)
class Mythread(Thread):
	def __init__(self,name):
		super().__init__()
		self.name=name
	def run(self):
		sema.acquire()
		print('Starting '+self.name)
		sleep(1)
		print('Exiting '+self.name)
		sema.release()
		
for i in range(1,26):
	Mythread('Thread_'+str(i)).start()
		

