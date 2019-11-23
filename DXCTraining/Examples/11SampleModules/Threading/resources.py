from threading import Thread,Lock
codelock=Lock()
class Mythread(Thread):
	target=open('target.txt','w')
	def __init__(self , source):
		super().__init__()
		self.source=source
	def run(self):
		codelock.acquire()
		for line in self.source:
			Mythread.target.write(line)
		self.source.close()
		codelock.release()
			
t1=Mythread(open('f1.txt','r'))
t2=Mythread(open('f2.txt','r'))
t1.start()
t2.start()
t1.join()
t2.join()
Mythread.target.close()