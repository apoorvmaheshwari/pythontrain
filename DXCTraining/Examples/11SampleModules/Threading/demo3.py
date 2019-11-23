from threading import Thread,activeCount,currentThread
class Mythread(Thread):
	def __init__(self,name):
		super().__init__()
		self.name=name
	def run(self):
		for i in range(1,100):
			print(self.name)
		
		
t1 = Mythread('Sachin')
t2 = Mythread('Rahul')
t1.start()
t2.start()
t1.join()
t2.join()
print(currentThread().getName())
print('count: ',activeCount())
print('Exiting MainThread!!!')