class entry_exit:
    
    def __init__(self, f):
        self.f = f
     
    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)

@entry_exit
def func1():
    print("inside func1()")

@entry_exit
def func2():
    print("inside func2()")
func1()
#func2()


'''def entry_exit(func):
	print('I am entering function')
	func.__call__()
	print('I am exiting function')
'''
