from threading import Thread,Condition
data=[]

def consumer(cv):
	while True:
		cv.acquire()
		while len(data)==0:
			print('We are waiting for item')
			cv.wait()
		print('We got an available item: '+str(data.pop(0)))
		cv.notify()
		cv.release()

def producer(cv):
	j=0
	while True:
		cv.acquire()
		while len(data)>=50:
			print('Basket is full , wait for space to produce')
			cv.wait()
		j+=1
		print('We are producing item')
		data.append('item'+str(j))
		cv.notify()
		cv.release()

def main():
    cv = Condition()
    Thread(target=consumer, args=(cv,)).start()    
    Thread(target=producer, args=(cv,)).start()

if __name__ == '__main__':
    main()