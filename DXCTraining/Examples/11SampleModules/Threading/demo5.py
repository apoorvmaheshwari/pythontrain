from threading import Thread,Condition
store=[]
storelock=Condition()
def producer(name):
	i=0
	while True:
		storelock.acquire()
		if len(store)<10:
			i+=1
			print(name+' is producing item_'+str(i))
			store.append(name+'_item_'+str(i))
		else :
			print('Store is full , '+name+' is waiting!')
			storelock.wait()
		storelock.notifyAll()
		storelock.release()
			
def consumer(name):
	while True:
		storelock.acquire()
		if len(store)>0:
			print(name+' is consuming '+store.pop(0))
		else :
			print('Store is empty , '+name+' is waiting!')
			storelock.wait()
		storelock.notify()
		storelock.release()
			
Thread(target=producer,args=('P1',)).start()
Thread(target=producer,args=('P2',)).start()
Thread(target=consumer,args=('C1',)).start()
Thread(target=consumer,args=('C2',)).start()
Thread(target=consumer,args=('C3',)).start()
Thread(target=consumer,args=('C4',)).start()



			