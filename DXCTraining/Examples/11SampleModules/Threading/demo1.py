from threading import Thread
def demo1():
	for i in range(1,1000):
		print('Sachin')
		
def demo2():
	for i in range(1,1000):
		print('Rahul')
		
t1 = Thread(target = demo1)
t2 = Thread(target = demo2)
t1.start()
t2.start()