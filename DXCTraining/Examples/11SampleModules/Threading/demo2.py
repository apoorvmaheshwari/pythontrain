from threading import Thread
def demo(name):
	for i in range(1,1000):
		print(name)
		

		
t1 = Thread(target = demo,args=('Sachin',))
t2 = Thread(target = demo,args=('Rahul',))
t1.start()
t2.start()