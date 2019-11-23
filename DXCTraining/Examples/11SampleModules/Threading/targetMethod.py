import threading

def loop1_10():
    for i in range(1, 1000):
       print(i)
def loop11_20():
    for i in range(1000, 2000):
        print(i)
 
t1= threading.Thread(target=loop1_10)
t2 = threading.Thread(target=loop11_20)
t1.start()
t2.start()