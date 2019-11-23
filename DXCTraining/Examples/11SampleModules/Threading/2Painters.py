from threading import Thread,Condition,Lock
import time
class brush:
	def __init__(self,name,loc):
		self.name=name
		self.loc=loc
		self.con=Condition(loc)

def painter1(brush1,brush2):
	brush1.con.acquire()
	time.sleep(1)
	print('Vinci is waiting for brush2!!!')
	while brush2.loc.locked():
			brush1.con.wait()
	brush2.con.acquire()
	print('Vinci has both brushes , vinci is painting!!!')
	brush2.con.notify()
	brush2.con.release()
	brush1.con.notify()
	brush1.con.release()

def painter2(brush1,brush2):
		brush2.con.acquire()
		time.sleep(1)
		print('Picasso is waiting for brush1!!!')
		while brush1.loc.locked():
			brush2.con.wait()
		brush1.con.acquire()
		print('Picasso has both brushes , Picasso is painting!!!')
		brush1.con.notify()
		brush1.con.release()
		brush2.con.notify()
		brush2.con.release()

def main():
	brush1=brush('brush1',Lock())
	brush2=brush('brush2',Lock())
	Thread(target=painter2, args=(brush1,brush2)).start()    
	Thread(target=painter1, args=(brush1,brush2)).start()

if __name__ == '__main__':
    main()