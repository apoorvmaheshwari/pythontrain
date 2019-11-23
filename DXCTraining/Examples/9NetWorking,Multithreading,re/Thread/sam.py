from threading import Thread,Condition


data=[]

def consumer(cv):
		cv.acquire()
		while len(data)==0:
			print('We are waiting for item')
			cv.wait()
		print('We got an available item: '+str(data.pop()))
		cv.release()

def producer(cv):
		i='item1'
		print('We are producing item')
		cv.acquire()
		data.append(i)
		cv.notify()
		cv.release()

def main():
    cv = Condition()
    Thread(target=consumer, args=(cv,)).start()    
    Thread(target=producer, args=(cv,)).start()

if __name__ == '__main__':
    main()